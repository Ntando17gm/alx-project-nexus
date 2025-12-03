from django.urls import path
from .views import PollViewSet

urlpatterns = [
    path('polls/', PollViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('polls/<int:pk>/', PollViewSet.as_view({'get': 'retrieve'})),
    path('polls/<int:pk>/vote/', PollViewSet.as_view({'post': 'vote'})),
]