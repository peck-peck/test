from django.shortcuts import render, get_object_or_404
from .models import Notification
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def notifications(request):
    template = loader.get_template('notifications/notifications.html')
    a ='a'

    notifications = Notification.objects.filter(user=request.user, is_seen=False).order_by('-id')
    notifications2 = Notification.objects.filter(user=request.user, is_seen=False).order_by('-id')

    for notification in notifications:
        notification.post_view +=1
        if notification.post_view > 1:
            notification.post_view -=1

        if notification.post_view >= 1:
            notification.is_seen = True
        else:
            notification.post_view = False
        notification.save()

        context = {

            'e': notification.is_seen,
            'notifications': notifications,

                   }
        return HttpResponse(template.render(context, request))

    context = {'notifications': notifications }
    return render(request, 'notifications/notifications.html', context)

def delete_notifications(request, notification_id):
    'Delete notification'
    notification = get_object_or_404(Notification, id=notification_id)

    if request.method == 'GET':
        notification.delete()
    return HttpResponseRedirect(reverse('show-notifications'))

