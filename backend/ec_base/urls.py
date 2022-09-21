from django.shortcuts import redirect
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

swagger_urlpatterns = [
    path("", lambda request: redirect("api/", permanent=True)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/", SpectacularSwaggerView.as_view(template_name="swagger-ui.html", url_name="schema"), name="swagger-ui"),
]

urlpatterns = swagger_urlpatterns + [
    path("api/auth/", include("ec_base.auth.urls"), name="auth"),
    path("api/master/", include("ec_base.master.urls"), name="master"),
]
