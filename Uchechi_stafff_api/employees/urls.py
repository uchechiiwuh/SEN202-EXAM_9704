from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagerViewSet, InternViewSet


router = DefaultRouter()
router.register(r'managers', ManagerViewSet)
router.register(r'interns', InternViewSet)


urlpatterns = [
    path('', include(router.urls)),
] 