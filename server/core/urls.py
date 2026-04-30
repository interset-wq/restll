from django.urls import path, include
from rest_framework import routers

from .views import TopicViewSet, EntryViewSet

router = routers.DefaultRouter()
router.register('topics', TopicViewSet)
router.register('entries', EntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
