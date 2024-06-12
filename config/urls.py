from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz_app.urls')),
    path('', include('login_register.urls')),
    path('', include('ecourse.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
