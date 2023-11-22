from django.urls import path

from .views import index, PostListView, PostDetailView, PostUpdateView, PostDeleteView, PostCreateView


urlpatterns = [
    path("",  index, name="home"),
    path("posts/", PostListView.as_view(), name='posts'),
    path("posts/<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    path("posts/update/<int:pk>/", PostUpdateView.as_view(), name='post-update'),
    path("posts/delete/<int:pk>/", PostDeleteView.as_view(), name='post-delete'),
    path("posts/create/", PostCreateView.as_view(), name='post-create'),

]