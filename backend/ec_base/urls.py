from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('api/', permanent=True)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/', SpectacularSwaggerView.as_view(template_name='swagger-ui.html', url_name='schema'), name='swagger-ui'),
    path('api/auth/', include('ec_base.auth.urls'), name='auth'),
    path('api/master/', include('ec_base.master.urls'), name='master'),
    path('api/customer/', include('ec_base.customer.urls'), name='customer'),
    path('api/discount/', include('ec_base.discount.urls'), name='discount'),
    path('api/product/', include('ec_base.product.urls'), name='product'),
    path('api/rating/', include('ec_base.rating.urls'), name='rating'),
    path('api/file-management/', include('ec_base.file_management.urls'), name='file-management'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
