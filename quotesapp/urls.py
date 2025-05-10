# quotesapp/urls.py
from django.urls import path
from .views import index_view, get_quote
from quotesapp import views

urlpatterns = [
    path('home/', index_view, name='home'),
    path('get-quote/',views.get_quote, name='get_quote'),
]