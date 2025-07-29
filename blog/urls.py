from django.urls import path
from blog.views import index,contato,template
urlpatterns = [
    path ("", index, name="index"),
    path("contato/", contato, name='contato'),
    path("template/", template, name='template'),
    ]

