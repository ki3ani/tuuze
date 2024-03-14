from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserProfileView, basename='userprofile')
router.register(r'stores', views.StoreViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'orderitems', views.OrderItemViewSet)
router.register(r'chatsessions', views.ChatSessionViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'subscriptions', views.SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
