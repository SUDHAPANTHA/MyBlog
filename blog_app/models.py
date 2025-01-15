from django.db import models
CHOICES =[
    ("active","Active"),
    ("inactive","Inactive")
]

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=False, null=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=CHOICES, default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

# Create your models here.
def __str__(self):
    return self.title
