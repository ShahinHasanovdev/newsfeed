from django.shortcuts import render,HttpResponse
from .models import Feed
# Create your views here.
def home(request):
    feeds =Feed.objects.all() #queryset
    context = {
        "feeds":feeds
    }
    return render(request, "feeds/home.html", context)
    #return HttpResponse(feeds)
