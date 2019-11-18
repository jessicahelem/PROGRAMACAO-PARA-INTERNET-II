from typing import Type

from django.shortcuts import render
from django.template.defaulttags import comment

from posts.models import *
import json
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.serializers import HyperlinkedModelSerializer

from posts.models import Post, Profile, Comment, Address
from posts.serializers import PostSerializer, ProfileSerializer, CommentSerializer, AddressSerializer, \
    ProfilePostSerializer, PostCommentSerializer


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'adress-list'



class AdressDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-detail'


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'


class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = ProfileSerializer
    name = 'comment-list'


class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-details'


class ProfilePostList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-posts-list'
    
class ProfilePostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name='profile-post-detail'

class PostCommentList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-list'


class PostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class =  PostCommentSerializer
    name = 'post-comment-detail'

class PostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class =  PostCommentSerializer
    name = 'post-comment-detail'





class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profiles': reverse(ProfileList.name, request=request),
            'address': reverse(AddressList.name, request=request),
            'posts': reverse(PostList.name, request=request),
            'profile-posts': reverse(ProfilePostList.name, request=request),
            'comments': reverse(PostCommentList.name, request=request),
           # 'profile-count:': reverse(ProfileCount.name, request=request),
        })

def import_archive():

    with open("comments.json", "r") as read_file:
        data = json.load(read_file)

    with open("users.json", "r") as read_file:
        data1 = json.load(read_file)

    with open("posts.json", "r") as read_file:
        data2 = json.load(read_file)

    with open("address.json","r") as read_file:
        data3 = json.load(read_file)

    for i in range(len(data['comments'])):
        comments = Comment()
        comments.body = data['comments'][i]["body"]
        comments.email = data['comments'][i]["email"]
        comments.postId = data['comments'][i]["postId"]
        comments.id = data['comments'][i]["id"]
        comments.name = data['comments'][i]["name"]
        comments.save()


    for i in range(len(data2['posts'])):
        posts = Post()
        posts.body = data2['posts'][i]["body"]
        posts.userId = data2['posts'][i]["userId"]
        posts.title = data2['posts'][i]["title"]
        posts.id = data2['posts'][i]["id"]
        posts.save()

    for i in range(len(data1['users'])):
        users = Profile()
        users.username = data1['users'][i]["username"]
        users.address = data1['address'][i]["id"]
        users.email = data1['users'][i]["email"]

        users.save()

        for post in data2['posts']:
            profile = Profile.objects.get(id=post['userId'])
            Comment.objects.create(id=comment['id'],name = comment['name'],email=comment['email'],body=comment['body'],post=post)