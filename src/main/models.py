from django.db import models

from users.models import User
from django.db import models

class UserLockerItem(models.Model):
    ITEM_TYPES = (
        ('outfit', 'Outfit'),
        ('emote', 'Emote'),
        ('pickaxe', 'Pickaxe'),
        ('backpack', 'Backpack'),
        ('glider', 'Glider'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locker_items')
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    video_url = models.URLField(blank=True, null=True)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES, default='outfit')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"
