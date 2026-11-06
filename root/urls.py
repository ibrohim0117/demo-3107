from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from apps.views import home_view, post_view
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('posts/', post_view, name='posts')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

