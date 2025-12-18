from django.db import models
import uuid

class FriendRequest(models.Model):
    friendID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    state = models.IntegerField(default=0)  # 0: pending, 1: accepted, -1: rejected
    requesterID = models.ForeignKey('home.User', on_delete=models.CASCADE, related_name='sent_friend_requests')
    receiverID = models.ForeignKey('home.User', on_delete=models.CASCADE, related_name='received_friend_requests')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Friend request from {self.requesterID.username} to {self.receiverID.username}"
