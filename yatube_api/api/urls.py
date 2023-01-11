from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, FollowViewSet, CommentViewSet, GroupViewSet


app_name = 'api'
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register(r'follow', FollowViewSet)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
