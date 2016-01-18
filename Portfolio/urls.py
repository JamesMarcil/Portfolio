from django.conf.urls       import patterns, include, url
from django.contrib         import admin
from django.views.generic   import RedirectView

from .views                 import IndexView, AboutView, ContactView

urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', IndexView.as_view(), name='index'),
        url(r'^about/', AboutView.as_view(), name='about'),
        url(r'^contact/', ContactView.as_view(), name='contact'),
        url(r'^projects/', include('projects.urls')),
        url(r'^resume/', RedirectView.as_view(url='http://jamesmarcil.com/static/resume.pdf')),
]
