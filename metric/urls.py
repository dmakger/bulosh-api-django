from django.urls import path, include
from rest_framework.routers import DefaultRouter

from metric.views import CategoryView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # Категория
    path("category/all/", CategoryView.as_view({'get': 'all'})),
]
