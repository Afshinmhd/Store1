from rest_framework.routers import DefaultRouter
from .views import CartAddViewSet, OrderCreateViewSet, OrderDetailViewSet

router = DefaultRouter()
router.register(r'cart', CartAddViewSet, basename='cart')
router.register(r'orderitem', OrderCreateViewSet, basename='cart')
router.register(r'order', OrderDetailViewSet, basename='cart')
urlpatterns = router.urls