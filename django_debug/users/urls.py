from django.urls import path
from users.views import django_toolbar
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', django_toolbar)
] + debug_toolbar_urls()