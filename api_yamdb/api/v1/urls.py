from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitleViewSet,
    UserViewSet,
    signup,
    token
)

v1_router = DefaultRouter()
v1_router.register('genres', GenreViewSet)
v1_router.register('titles', TitleViewSet)
v1_router.register('categories', CategoryViewSet)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
v1_router.register('users', UserViewSet)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', signup, name='auth_signup'),
    path('v1/auth/token/', token, name='auth_token')
]
