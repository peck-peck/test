from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import JobAlert, Announcement


# Create your views here.

def job_ads(request):
    job_ads = JobAlert.objects.order_by('-id')
    ads_counter = len(job_ads)

    page = request.GET.get('page', 1)
    paginator = Paginator(job_ads, 20)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'job_ads': posts, 'count_job_ads': ads_counter}
    return render(request, 'advertisement/job_ads.html', context)


def ads_user_city(request, shop_id):
    user = User.objects.get(id=shop_id)
    job_ads = JobAlert.objects.filter(company_city=user.shop.city).order_by('-id')
    ads_counter = len(job_ads)

    page = request.GET.get('page', 1)
    paginator = Paginator(job_ads, 20)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'advertisement/user_city_ads.html',
                  {'job_ads': posts,
                   'user': user,
                   'count_user_city_ads': ads_counter
                   }
                  )


def ads_user_country(request, shop_id):
    user = User.objects.get(id=shop_id)
    job_ads = JobAlert.objects.filter(company_country=user.shop.country).order_by('-id')
    ads_counter = len(job_ads)

    page = request.GET.get('page', 1)
    paginator = Paginator(job_ads, 20)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'advertisement/user_country_ads.html',
                  {'job_ads': posts,
                   'user': user,
                   'count_user_country_ads': ads_counter
                   }
                  )


def announcements(request):
    announcement = Announcement.objects.order_by('-id')
    context = {'announcements': announcement}
    return render(request,'advertisement/announcements.html', context)

