from django.urls import path
from .views import add_post_view, update_post_view, DeletePostView, home_view, post_detail_view
urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', home_view, name='home'),
    # path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>', post_detail_view, name='post-detail'),
    # path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_post/', add_post_view, name='add_post'),
    # path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/edit/<int:pk>', update_post_view, name='update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete-post')
]
