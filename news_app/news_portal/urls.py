from django.urls import path
from .views import PostList, PostDetail


urlpatterns = [
   path('', PostList.as_view()),
   path('<id>', PostDetail.as_view()),
]
