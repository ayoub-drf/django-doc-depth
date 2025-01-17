from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT)
    def __str__(self):
        return f'{self.user.username}'

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    def __str__(self):
        return f'Post ID: {self.pk} | {self.author}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    def __str__(self):
        return f'Comment ID: {self.pk} | Post ID: {self.post.pk} | commenter: {self.commenter}'


