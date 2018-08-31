#from .views import tweet_detail_view, tweet_list_view
from django.conf.urls import url
#from .views import TweetDetailView,TweetListView, TweetCreateView, TweetUpdateView, TweetDeleteView
from django.views.generic import RedirectView
from .views import TweetListAPIView, TweetCreateAPIView
urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'),  #/api/tweet/
    # url(r'^$', RedirectView.as_view(url='/')),
    # url(r'^search/$', TweetListView.as_view(), name='list'),  #/tweet/
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), #/tweet/create/
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), #/tweet/1/
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), #/tweet/1/update
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), #/tweet/1/delete
]
