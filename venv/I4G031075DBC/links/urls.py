from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.allLinks),
    
    path('', views.PostListApi),
    path("add/", views.PostCreateApi),
    path("<str:id>/", views.PostDetailApi),
    path("del/<str:id>/", views.PostDeleteApi),
    path("update/<str:id>/", views.PostUpdateApi),
    path("active/", ActiveLinkView.as_view(), name=’active_link’),
    path("recent/", RecentLinkView.as_view(), name=’recent_link’),
]