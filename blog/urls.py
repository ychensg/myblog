from django.urls import include,path
from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('post/<int:id>',views.Detail,name="blog_detail"),
    path('home/',views.Home,name="blog_home"),
    path('test/',views.Test,name="blog_test"),
    path('', RedirectView.as_view(url="/home")),
]
