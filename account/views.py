from django.views.generic import TemplateView

class AccountView(TemplateView)
    template_name = 'account/index.html'

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        user = self.request.user
        context['orders'] = user.order_set.all()
        return context
