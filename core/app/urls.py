from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_views),
    path('music/<int:pk>/', views.music_detail_view, name='detail')
]