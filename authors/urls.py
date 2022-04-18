from django.urls import path

from authors.views import index_author

urlpatterns = [
    path('', index_author),
]