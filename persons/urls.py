from django.urls import path, include
from rest_framework_nested import routers

from persons.views import PersonViewSet, IntroductionViewSet, DescriptionViewSet

router = routers.SimpleRouter()
router.register(r'', PersonViewSet)

nested_router = routers.NestedSimpleRouter(router, r'', lookup='person')
nested_router.register(r'introduction', IntroductionViewSet, basename='introduction')
nested_router.register(r'description', DescriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
