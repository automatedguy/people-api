from django.urls import path, include
from rest_framework_nested import routers

from persons.views import PersonViewSet, IntroductionViewSet, DescriptionViewSet, PhotoViewSet, VideoViewSet

router = routers.SimpleRouter()
router.register(r'', PersonViewSet)


nested_router = routers.NestedSimpleRouter(router, r'', lookup='person')
nested_router.register(r'introduction', IntroductionViewSet)
nested_router.register(r'description', DescriptionViewSet)
nested_router.register(r'photos', PhotoViewSet)
nested_router.register(r'videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
