from django.urls import path
from .views import PostList, PostDetail, SearchList, PostCreate, PostDelete, PostUpdate


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>/', PostDetail.as_view()),
   path('search/', SearchList.as_view()),
   path('post_create/', PostCreate.as_view()),
   path('<int:pk>/post_edit/', PostUpdate.as_view()),
   path('<int:pk>/post_delete/', PostDelete.as_view()),
   path('article/post_create/', PostCreate.as_view()),
   path('article/<int:pk>/post_edit/', PostUpdate.as_view()),
   path('article/<int:pk>/post_delete/', PostDelete.as_view()),

]
