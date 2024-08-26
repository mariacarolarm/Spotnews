from django.urls import path
from .views import index, new_category, new_news, news

urlpatterns = [
  path('', index, name='home-page'),
  path('news/<int:id>/', news, name='news-details-page'),
  path('categories/', new_category, name='categories-form'),
  path('news/', new_news, name='news-form')
]
