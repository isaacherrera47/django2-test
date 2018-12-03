# Create your views here.
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, UpdateView

from movies.forms import ReviewForm
from movies.models import Review


class ReviewListView(ListView):
    model = Review
    template_name = 'movies/index.html'


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'movies/detail.html'


class ReviewCreateView(PermissionRequiredMixin, FormView):
    permission_required = 'is_superuser'
    form_class = ReviewForm
    template_name = 'movies/new_edit.html'
    success_url = reverse_lazy('review-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'is_superuser'
    model = Review
    form_class = ReviewForm
    template_name = 'movies/new_edit.html'
    success_url = reverse_lazy('review-list')

