from django.urls import path,re_path
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('', views.productViewSet, base_name='product')
# router.register('reviews/', views.feedbackViewSet, base_name='feedback')

# urlpatterns = router.urls


urlpatterns = [
    path('',views.ProductList.as_view()),
    re_path('(?P<number>.+)/', views.ReviewList.as_view()),
    
]