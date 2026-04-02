from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecordViewSet, DashboardView

router = DefaultRouter()
router.register("records", RecordViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("dashboard/", DashboardView.as_view()),
]