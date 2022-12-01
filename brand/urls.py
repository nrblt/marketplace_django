from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BrandViewSet

router = SimpleRouter()
router.register("",BrandViewSet)

urlpatterns = router.urls
