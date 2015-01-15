from django.conf.urls import patterns, include, url
from django.contrib import admin
from user import views
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'registraion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.loginpage, name = 'LoginPage'),
    url(r'^signup/', views.signuppage, name = 'SignupPage'),
    url(r'^profile/', views.profilepage, name = 'UserPage'),
    url(r'^editpage/', views.editpage, name = 'editpage'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page' : 'LoginPage' }),
    url(r'^loggedout/', views.loginpage, name = 'loggedout'),
    url(r'^error_page/', views.errorpage, name = 'ErrorPage'),
    url(r'^superuser/', views.superpage, name = 'SuperUser'),
    url(r'^delete/',views.delete, name = 'DeleteUser'),
    url(r'^search/', views.searchbox, name = "Search_box"),
    url(r'^searchbox/', views.searchauto, name = "searchbox"),
    (r'^accounts/', include('registration.backends.default.urls')),

    
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
)
