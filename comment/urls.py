from rest_framework.routers import SimpleRouter

from .views import CommentViewSet

router = SimpleRouter()
router.register("",CommentViewSet)


urlpatterns = router.urls
