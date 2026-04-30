from rest_framework import viewsets

from .models import Topic, Entry
from .serializers import TopicSerializer, EntrySerializer


# Create your views here.
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer