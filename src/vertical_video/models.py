from django.db import models
import uuid

from users.models import SocialMediaAccount

class VerticalVideo(models.Model):
    """TikTok-like vertical video feed item"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=225)
    user = models.ForeignKey(
        to=SocialMediaAccount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="videos"
    )
    likes = models.IntegerField(default=0)

    video_file = models.FileField(upload_to="videos/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.user.username if self.user else 'Unknown'}"