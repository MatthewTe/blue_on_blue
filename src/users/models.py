from django.db import models
import uuid

class SocialMediaAccount(models.Model):
    """Basic independent social media user model"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    # Social graph
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="following", blank=True
    )

    date_joined = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username