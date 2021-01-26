from django.urls import path

from .apis import ItemView


urlpatterns = [
    path('', ItemView.as_view(), name='items')
]
