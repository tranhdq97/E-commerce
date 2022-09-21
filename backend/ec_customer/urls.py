"""ec_staff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

handler500 = "ec_base.common.custom.exceptions.server_error"

urlpatterns = [
    path("", include("ec_base.urls")),
    path("api/customer/", include("ec_customer.customer.urls"), name="customer"),
    path("api/order/", include("ec_customer.order.urls"), name="order"),
    path("api/product/", include("ec_customer.product.urls"), name="product"),
]
