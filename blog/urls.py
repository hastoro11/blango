from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path("post/<slug>/", views.post_detail, name="blog-post-detail")

]