from django.urls import re_path
from django.urls import path
from . import views
from django.contrib import admin


urlpatterns=[
    # path("greet/", views.say_hello),
    re_path(r"^$", views.home),
    path('admin/', admin.site.urls),
    path('servefile/', views.serve_req),
]