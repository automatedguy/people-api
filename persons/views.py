from rest_framework.viewsets import ModelViewSet

from .models import Person, Introduction, Description
from .serializers import PersonSerializer, IntroductionSerializer, DescriptionSerializer


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonFilterViewSet(ModelViewSet):

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(person=self.kwargs.get('person_pk'))


class IntroductionViewSet(PersonFilterViewSet):
    serializer_class = IntroductionSerializer
    queryset = Introduction.objects.all()


class DescriptionViewSet(PersonFilterViewSet):
    serializer_class = DescriptionSerializer
    queryset = Description.objects.all()

