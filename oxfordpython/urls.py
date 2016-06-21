from django.conf.urls import url
from django.contrib import admin

from main import views as main_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.HomeView.as_view(), name='home'),
]
