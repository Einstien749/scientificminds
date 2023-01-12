from django.db import models

from django.contrib.auth import get_user_model
# Create your models here.

class Category(models.Model):

    category = models.CharField(choices = (("mathematics","mathematics"),("physics","physics"),("web_development","web_development"),("programming","programming"), ("personality","personality"), ("politics","politics"), ("football","football")), max_length=20)

    def __str__(self):

        return str(self.category)

class Post(models.Model):

    title = models.CharField(max_length = 20)

    description = models.TextField()

    postimg = models.ImageField(upload_to = 'images')

    dateposted = models.DateTimeField(auto_now = True)

    posturl = models.CharField(max_length=50, unique = True)

    text = models.TextField(null= True, blank= True, max_length=1000000000)

    category = models.ForeignKey(Category,on_delete = models.CASCADE, null=True, blank=True)



    def __str__(self):

        return str(self.title)


class Quote(models.Model):

    quote = models.TextField()

    author = models.CharField(max_length = 20)

    author_img = models.ImageField(upload_to = 'quotes')


    def __str__(self):

        return str(self.author)

class Comment(models.Model):

    comment = models.TextField(null=False, blank=False)

    writer = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)

    comment_date = models.DateTimeField(auto_now = True)

    def __str__(self):

        return str(self.writer)

class PostComment(models.Model):

    postcomment = models.TextField(null=False, blank=False)

    writer = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)

    postitem = models.ForeignKey(Post, on_delete= models.CASCADE)
    
    comment_date = models.DateTimeField(auto_now = True)

    def __str__(self):

        return str(self.writer)

