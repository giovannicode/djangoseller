from django.db.models import Q
from django.views.generic import TemplateView

from orders.models import Order

class AccountView(TemplateView):
    template_name = 'account/index.html'

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        user = self.request.user
        context['orders'] = Order.objects.filter(Q(user=user) | Q(user=None, email=user.email))
        return context
