from django.urls import path

from advertisement.views import job_ads, ads_user_city, ads_user_country,announcements

app_name = 'announcements'
urlpatterns = [
    # show all jobs advertisements
    path('job_advertisement/', job_ads, name='job_ads'),
    path('ads_at_user_city/<int:shop_id>/', ads_user_city, name='ads_user_city'),
    path('ads_at_user_country/<int:shop_id>/', ads_user_country, name='ads_user_country'),
    path('announcements/', announcements, name='announcements')

]