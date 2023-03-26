from django.urls import path
from .views import MusicListCreateView, MusicRetrieveUpdateDestroyView, MusicLikeView

urlpatterns = [
    path('music/', MusicListCreateView.as_view(), name='music-list-create'),
    path('music/<int:pk>/', MusicRetrieveUpdateDestroyView.as_view(),
         name='music-retrieve-update-destroy'),
    path('music/<int:pk>/like/', MusicLikeView.as_view(), name='music-like-update')
]
