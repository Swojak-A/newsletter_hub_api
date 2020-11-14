"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from typing import List

from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = _("Newsletter Hub API")

handler404 = "modules.core.views.errors.page_not_found"
handler500 = "modules.core.views.errors.server_error"
handler403 = "modules.core.views.errors.permission_denied"
handler400 = "modules.core.views.errors.bad_request"

urlpatterns: List = []

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls), prefix_default_language=False
)

if settings.APP_ENV in ("dev", "stage"):
    from modules.core.views.api_health_check import api_health_check

    urlpatterns += [path("check/", api_health_check, name="api-health-check")]
