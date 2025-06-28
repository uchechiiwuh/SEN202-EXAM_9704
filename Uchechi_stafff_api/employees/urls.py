from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagerViewSet, InternViewSet, AddressViewSet



router = DefaultRouter()
router.register(r'managers', ManagerViewSet, basename='manager')
router.register(r'interns', InternViewSet, basename='intern')
router.register(r'addresses', AddressViewSet, basename='address')


urlpatterns = [
    path('', include(router.urls)),
] 