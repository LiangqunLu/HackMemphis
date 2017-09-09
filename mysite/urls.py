"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import view, search

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^polls/', include('polls.urls')),

    url(r'^housing/', include('housing.urls')),

    url(r'^roommate/', include('roommate.urls')),
    url(r'^carpool/', include('carpool.urls')),
    url(r'^studygroup/', include('studygroup.urls')),

    url(r'^contact/', include('contact.urls')),

    url(r'^login/', include('login.urls')),

    #url(r'^admin/', admin.site.urls),
    url(r'^hello$', view.hello),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


