from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import CommentApiView, ReviewApiListView, ReviewDetailListView

app_name = 'api'
urlpatterns = [
    path('comments/', CommentApiView.as_view(), name='comments'),
    path('reviews/', ReviewApiListView.as_view(), name='reviews'),
    path('reviews/<int:pk>', ReviewDetailListView.as_view(), name='review-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
