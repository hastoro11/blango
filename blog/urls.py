from django.urls import path, include
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path("post/<slug>/", views.post_detail, name="blog-post-detail"),
    path("accounts/", include("django.contrib.auth.urls")),
]