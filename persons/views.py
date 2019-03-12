from rest_framework.viewsets import ModelViewSet

from .models import Person, Introduction
from .serializers import PersonSerializer, IntroductionSerializer


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class IntroductionViewSet(ModelViewSet):
    serializer_class = IntroductionSerializer
    queryset = Introduction.objects.all()
