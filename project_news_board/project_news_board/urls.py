from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import url

from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('desk/', include('desk.urls', namespace='desk')),
    path('', include('desk.urls', namespace='desk')),
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),

]
