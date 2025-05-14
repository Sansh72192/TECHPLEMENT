# quotesapp/urls.py
# project_root/urls.py
# quotesapp/urls.py
from django.urls import path
from .views import index_view, get_quote

urlpatterns = [
    path('', index_view, name='home'),            # <-- this will handle base path
    path('home/', index_view, name='home'),       # still allows /home/
    path('get-quote/', get_quote, name='get_quote'),
]
