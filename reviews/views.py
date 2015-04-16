from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView

from .models import Review
from .forms import ReviewForm

from products.models import Product

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
 
    def get_context_data(self, **kwargs):
        context = super(ReviewCreateView, self).get_context_data(**kwargs)
        context['product_id'] = self.kwargs['product_id'] 
        return context

    def form_valid(self, form):
        review = form.save(commit=False)
        review.user = self.request.user
        review.product = Product.objects.get(pk=self.kwargs['product_id']) 
        review.save() 
        return redirect('account:index')


class ReviewListView(ListView):
    model = Review

    def get_queryset(self):
        product = Product.objects.get(pk=self.kwargs['product_id'])
        return Review.objects.filter(product=product)
