from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include('main_store.urls')),
    path('', include('login_register.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main_store.views.error_404'
handler403 = 'main_store.views.error_403'