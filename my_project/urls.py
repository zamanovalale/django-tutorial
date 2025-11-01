from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!")

urlpatterns = [
    path("", home),  # <– boş URL üçün sadə səhifə
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
