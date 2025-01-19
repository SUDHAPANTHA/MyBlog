from django.db import models
from django.utils.timezone import now

# Status choices for the post
CHOICES = [
    ("active", "Active"),
    ("inactive", "Inactive"),
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

    def __str__(self):
        return self.title

    def publish(self):
        """
        Mark the post as active and set the published date.
        """
        self.status = "active"
        self.published_at = now()
        self.save()

    def deactivate(self):
        """
        Mark the post as inactive.
        """
        self.status = "inactive"
        self.save()

    class Meta:
        ordering = ["-created_at"]  
