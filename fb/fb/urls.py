from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from aldown import urls as al_urls
from twishare import urls as twi_urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fb.views.home', name='home'),
    # url(r'^fb/', include('fb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^aldown/',include(al_urls)),
	(r'^twishare/',include(twi_urls)),

)
urlpatterns += patterns('django.views.generic.simple',
    (r'^aldown-from-id.html$',             'direct_to_template', {'template': 'aldown-from-id.html'}),
    (r'^twishare.html$',             'direct_to_template', {'template': 'twishare-home.html'}),
	
)
urlpatterns += staticfiles_urlpatterns()
