from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from restaurants.views import RestaurantView, ReviewView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'reviews', ReviewView, basename='reviews')
router.register(r'restaurants', RestaurantView, basename='restaurants')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
