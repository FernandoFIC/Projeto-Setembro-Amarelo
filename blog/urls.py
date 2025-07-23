from django.urls import path
from blog.views import index
#create your views here
urlpatterns = [
    path ("", index, name="index"),

    ]

