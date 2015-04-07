from django import forms
from django.db import transaction, IntegrityError
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib import messages

from braces.views import AnonymousRequiredMixin
from users.models import User
from users.forms import UserCreateForm
from carts.models import Cart

from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import ugettext as _
from django.template.response import TemplateResponse


class UserCreateView(AnonymousRequiredMixin, CreateView):
    authenticated_redirect_url = u"/"
    model = User
    form_class = UserCreateForm
    success_url = 'main:index'

    def form_valid(self, form): 
        try:
            with transaction.atomic():
                cart = Cart.objects.create()
                user = form.save(commit=False)
                user.cart = cart
                user.save()
               
        except IntegrityError:
            messages.add_message(
                self.request,
                messages.INFO,
                'I\'m sorry an unkown error occured'
            )
   
        user = authenticate(
            username=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password1')
        )
        login(self.request, user)
        return redirect('main:index')


class UserLoginView(AnonymousRequiredMixin, FormView):
    authenticated_redirect_url = u"/"
    template_name = 'users/login.html'
    form_class = AuthenticationForm
  
    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('main:index')


class ForgotPasswordView(FormView):
    template_name = 'users/forgot_password.html'
    form_class = PasswordResetForm
    success_url = '/users/signin'

    def form_valid(self, form):
        email_template_name='emails/reset_password_link.html'
        from_email='gio@seller.org'
        form.save(request=self.request, email_template_name=email_template_name)
        return super(ForgotPasswordView, self).form_valid(form)

# In future add decorators (sensitive_post_parameters, never_cache)
class ResetPasswordView(FormView):
    template_name = 'users/reset_password.html'
    form_class = SetPasswordForm

    def get_form(self, form_class):
        uidb64 = self.kwargs['uidb64'] 
        token = self.kwargs['token']
        UserModel = get_user_model()
        token_generator=default_token_generator
        
        assert uidb64 is not None and token is not None #checked by URLFconf
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoestNotExist):
            user = None
        if user is not None and token_generator.check_token(user, token):
            return form_class(user, **self.get_form_kwargs())

    def form_valid(self, form):
        form.save()    
	return redirect('users:signin')


@sensitive_post_parameters()
@never_cache
def password_reset_confirm(request, uidb64=None, token=None,
                           template_name='users/reset_password.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           post_reset_redirect=None,
                           current_app=None, extra_context=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    UserModel = get_user_model()
    assert uidb64 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
       post_reset_redirect = reverse('main:index')
       # post_reset_redirect = reverse('password_reset_complete')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        title = _('Enter new password')
        if request.method == 'POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(post_reset_redirect)
        else:
            form = set_password_form(user)
    else:
        validlink = False
        form = None
        title = _('Password reset unsuccessful')
    context = {
        'form': form,
        'title': title,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


def signout(request):
    logout(request)
    return redirect('main:index')
