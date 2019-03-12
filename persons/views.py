from rest_framework.viewsets import ModelViewSet

from .models import Person, Introduction, Description
from .serializers import PersonSerializer, IntroductionSerializer, DescriptionSerializer


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class IntroductionViewSet(ModelViewSet):
    serializer_class = IntroductionSerializer
    queryset = Introduction.objects.all()


class DescriptionViewSet(ModelViewSet):
    serializer_class = DescriptionSerializer
    queryset = Description.objects.all()
