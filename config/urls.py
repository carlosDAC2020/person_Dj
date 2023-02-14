
from django.contrib import admin
from django.urls import path,include
from person.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index),
    path('person/',include('person.urls'))
]
