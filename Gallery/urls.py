from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^gallery/$',views.welcome,name = 'welcome'),
    url(r'^today/$',views.news_of_day,name='newsToday'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews') ]
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews') 
    url(r'^$',views.galler,name = 'galler'),
    url(r'^search/$',views.search_results,name='search_results'),
    url(r'^image/(\d+)',views.image,name='image'),
    url(r'^location/(\d+)',views.filter_by_location,name='location'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
