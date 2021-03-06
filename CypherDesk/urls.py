from django.contrib import admin
from django.conf.urls import include, handler404, handler500
from django.urls import path
from LandPage import views as Landpage_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('LandPage.urls')),
    path('custom_admin/', include('AdminPanel.urls')),
    path('standart_admin/', admin.site.urls),
    path('feedback/', include('Feedback.urls')),
    path('news/', include('News.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = Landpage_views.error_403
handler404 = Landpage_views.error_404
handler500 = Landpage_views.error_500