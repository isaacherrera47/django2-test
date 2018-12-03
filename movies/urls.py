from django.urls import path

from movies.views import ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView

urlpatterns = [
    path('', ReviewListView.as_view(), name='review-list'),
    path('<slug:pk>', ReviewDetailView.as_view(), name='review-detail'),
    path('create/', ReviewCreateView.as_view(), name='review-create'),
    path('edit/<slug:pk>', ReviewUpdateView.as_view(), name='review-edit'),
]
