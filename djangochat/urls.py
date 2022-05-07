from django.contrib import admin
from django.urls import path, include
import login
from login import urls
import chat
from chat import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(login.urls)),
    path('', include(chat.urls)),
    
    # path('travel',include(travel.urls)),
]