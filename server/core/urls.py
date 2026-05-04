from django.urls import path, include
from rest_framework import routers

from .views import TopicViewSet, EntryViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('topics', TopicViewSet)
router.register('entries', EntryViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
