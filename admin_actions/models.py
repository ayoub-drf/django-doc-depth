from django.db import models

STATUS_CHOICES = {
    "d": "Draft",
    "p": "Published",
    "w": "Withdrawn",
}


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="d")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title