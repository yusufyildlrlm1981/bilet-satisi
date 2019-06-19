 
from django.conf.urls import url
from django.contrib import admin
from ticketAgent import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
                url(r'^admin/', admin.site.urls),
                url(r'^$', views.login, name='home'),
                url(r'^events/$', views.events, name='events'),
                url(r'^signup/$', views.signup, name='signup'),
                url(r'^browse/$', views.browse, name='browse'),
                url(r'^myreservations/$', views.myReservations, name='myReservations'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
