"""Post URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from posts import views
from posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ApiRoot.as_view(), name=ApiRoot.name),
    path('profile/',ProfileList.as_view(),name=ProfileList.name),
    path('posts/', views.PostList.as_view(), name=views.PostList.name),
    path('address/',AddressList.as_view(),name=AddressList.name),
    path('profile/<int:pk>',ProfileDetails.as_view(),name=ProfileDetails.name),
    path('posts<int:pk>',PostDetails.as_view(),name=PostDetails.name),
    path('address<int:pk>',AdressDetails.as_view(),name=AdressDetails.name),
    path('profile-post/',ProfilePostList.as_view(),name=ProfilePostList.name),
    path('profile-post/<int:pk>', ProfilePostDetail.as_view(), name=ProfilePostDetail.name),
    path('posts-comments/', PostCommentList.as_view(), name=PostCommentList.name),
    path('post-comments/<int:pk>', PostCommentDetail.as_view(), name=PostCommentDetail.name),
    path

]
