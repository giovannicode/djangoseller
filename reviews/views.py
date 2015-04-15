from django.shortcuts import render
from django.views.generic import CreateView

from .models import Review

class ReviewCreateView(CreateView):
    model = Review
