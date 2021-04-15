from django.urls import path, include

urlpatterns = [
    path('/', include('lazy_loading.urls')),
    path('/<int:param>', include('lazy_loading.urls')),
]