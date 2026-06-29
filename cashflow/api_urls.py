from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r"statuses", api_views.StatusViewSet)
router.register(r"types", api_views.TypeViewSet)
router.register(r"categories", api_views.CategoryViewSet)
router.register(r"subcategories", api_views.SubcategoryViewSet)
router.register(r"records", api_views.CashFlowRecordViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
