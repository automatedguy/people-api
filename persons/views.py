from rest_framework.viewsets import ModelViewSet

from .models import Person, Introduction, Description, ContactInfo
from .serializers import PersonSerializer, IntroductionSerializer, DescriptionSerializer, ContactInfoSerializer


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonFilterViewSet(ModelViewSet):

    _filter_ = 'person_pk'

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(person=self.kwargs.get(self._filter_))


class IntroductionViewSet(PersonFilterViewSet):
    serializer_class = IntroductionSerializer
    queryset = Introduction.objects.all()


class DescriptionViewSet(PersonFilterViewSet):
    serializer_class = DescriptionSerializer
    queryset = Description.objects.all()


class ContactInfoViewSet(PersonFilterViewSet):
    serializer_class = ContactInfoSerializer
    queryset = ContactInfo.objects.all()


