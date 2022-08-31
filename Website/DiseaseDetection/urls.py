from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
    path('disease/',include('cancer.urls')),
    path('users/',include('users.urls')),
    path('eye/',include('eye.urls')),
    path('heart-disease/',include('heart.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)