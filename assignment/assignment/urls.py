from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('faq.urls')),  # API routes for FAQs
    path('', include('faq.urls')),  # Ensure root URL works
]
