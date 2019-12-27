from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = 'Test platform Admin'
admin.site.site_header = 'Test platform Admin'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls')),
    path('adminboard/', include('adminboard.urls')),
    path('api/v1/', include('social_django.urls', namespace='social')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)