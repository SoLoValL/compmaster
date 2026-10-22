"""
URL configuration for compmaster project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('api/services/', include('apps.services.urls')),
    path('api/requests/', include('apps.requests.urls')),
    path('api/portfolio/', include('apps.portfolio.urls')),
    path('api/calculator/', include('apps.calculator.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/blog/', include('apps.blog.urls')),
    path('api/reviews/', include('apps.reviews.urls')),
    path('api/auth/', include('apps.users.jwt_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
