from django.db import models


# Create your models here.
import Post


class Address(models.Model):
    street = models.CharField(max_length=255, null=False)
    suite = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=False)
    zipcode = models.CharField(max_length=255, null=False)


class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    body = models.CharField(max_length=200, null=False)
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


