"""UCLeague URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Django core Import
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

# Yet another swagger import 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Local Import
from .constants import *

schema_view = get_schema_view(
   openapi.Info(
      title=DOCS_TITLE,
      default_version=DOCS_VERSION,
      description=DOCS_DESCRIPTION,
      terms_of_service=DOCS_TERM_SERVICE,
      contact=openapi.Contact(email=DOCS_CONTACT_HEAD),
      license=openapi.License(name=DOCS_LICENSE),
   ),
   public=DOCS_VISIBLE_PUBLIC
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include('app.club.urls', namespace='club_fetch')),

    url(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='docs-json'),
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='docs-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
