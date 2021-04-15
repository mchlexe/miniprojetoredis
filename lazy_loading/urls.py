from django.urls import path, include

urlpatterns = [
    path('/<int:param>', include('lazy_loading.urls')),
]