from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('pages.urls')),
    path('bars/', include('bars.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('store/', include('store.urls')),
    
    path('chatbot/', include('chatbot.urls')),
    path('inventory/', include('inventory.urls')),
    path('api/', include('api.urls')),
    # path('paypalRest/', include('paypalRest.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
