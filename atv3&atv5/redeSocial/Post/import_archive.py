import profile

from django.template.defaulttags import comment

from posts.models import *
import json


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