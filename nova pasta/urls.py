from django.urls import path
from notifications.views import notifications,delete_notifications


urlpatterns=[
    path('notifications/', notifications, name='show-notifications'),
    path('delete_notifications/<int:notification_id>/',delete_notifications, name='delete_notifications')
]