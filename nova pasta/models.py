from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Notification(models.Model):
    Notification_Type = ((1, 'like'), (2, 'comment'), (3, 'follow'), (4, 'reply'), (5, 'cart'))
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='noti_post', blank=True)
    # usuario que comentou
    sender = models.ForeignKey(User, related_name='noti_from_user', on_delete=models.CASCADE)
    # usuario dono do post
    user= models.ForeignKey(User, related_name='noti_to_user', on_delete=models.CASCADE)
    notification_type = models.IntegerField(choices=Notification_Type)
    text_preview = models.CharField(max_length=90, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
    #comment_id=models.CharField(User,max_length=90, blank=True)
    post_view = models.IntegerField(default=0,blank=True)
