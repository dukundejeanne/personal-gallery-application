from django.shortcuts import render
import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Image,Location,
# from .models import Image,Location,Photographer,Category
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today-news.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def past_days_news(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past-news.html', {"date": date})

def location (request,location_id):
    location=Image.objects.filter(location_id=location_id)
    return render(request,'location.html',{"location":location})




def galler(request):
    images=Image.objects.all()
    return render(request,'galler.html',{'images':images})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term=request.GET.get("image")
        searched_photos=Image.search_by_category(search_term)
        message=f'{search_term}'

        return render(request,"all-photo/search.html",{"message":message,"photos":searched_photos})
    else:
        message="you have no seach Photo"
        return render(request,'all-photo/search.html',{"message":message})

def image(request,image_id):
    try:
        image=Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render (request,"all-photo/image.html",{"image":image})

def filter_by_location(request,location_id):
    images=Image.filter_by_location(id=location_id)
    return render(request,'location.html',{"images":images})

# Create your views here.
# def fashion(request):
#     images = Image.objects.all()
#     return render(request, 'fashion.html',{'images':images})

# def search_results(request):
    
#     if 'image' in request.GET and request.GET["image"]:
#         search_term = request.GET.get("image")
#         searched_photos = Image.search_by_category(search_term)
#         message = f"{search_term}"

#         return render(request, 'all-photo/search.html',{"message":message,"photos": searched_photos})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all-photo/search.html',{"message":message})

# def image(request,image_id):
#     try:
#         image = Image.objects.get(id = image_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"all-photo/image.html", {"image":image})
# def filter_by_location(request,location_id):
#    """
#    Function that filters images by location
#    """
#    images = Image.filter_by_location(id=location_id )
#    return render (request, 'location.html', {"images":images})