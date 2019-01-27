from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'simplemooc.core.views.home', name='home'),
    url(r'^contato/$','simplemooc.core.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
]
