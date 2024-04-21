from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ad.views import PosterView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    path("poster/all/", PosterView.as_view({'get': 'all'})),
]
