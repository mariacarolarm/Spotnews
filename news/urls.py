from django.urls import path
from .views import index, news

urlpatterns = [
  path('', index, name='home-page'),
  path('news/<int:id>/', news, name='news-details-page'),
]
