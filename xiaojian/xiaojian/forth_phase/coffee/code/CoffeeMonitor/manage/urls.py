
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    #防止路由被截取
    url('map', views.map_views),
    # path('download.html', views.download),
    # path('login.html', views.login),
    # path('<int:id>.html', views.model_index)
]
