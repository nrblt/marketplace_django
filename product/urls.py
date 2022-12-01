from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import DislikesViewSet, LikesViewSet, ProductViewSet

router = SimpleRouter()

router.register("",ProductViewSet)
router.register("likes",LikesViewSet)
router.register("dislikes",DislikesViewSet)

urlpatterns = router.urls
