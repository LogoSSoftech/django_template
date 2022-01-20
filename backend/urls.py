
from django.urls import path
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
path('api/core/', include('core.urls')),
path('auth/', include('djoser.urls.authtoken')),
path('auth/', include('djoser.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


