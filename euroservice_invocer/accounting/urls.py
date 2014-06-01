from django.conf.urls import patterns, include, url

from rest_framework.routers import DefaultRouter

from .customers.apiviews import CustomerViewSet


router = DefaultRouter()
router.register('customers', CustomerViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
