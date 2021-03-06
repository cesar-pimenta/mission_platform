from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('navigation.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
