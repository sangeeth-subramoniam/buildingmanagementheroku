from django.urls import path,include
from . import views

app_name = 'setprice'
urlpatterns = [
    path('', views.home , name = "home"),
    path('setprice_update_form/<int:pk>', views.updateSetPriceForm , name = 'updateSetPriceForm'),
    path('setprice_delete_form/<int:pk>', views.deleteSetPriceForm , name = 'deleteSetPriceForm'),
]
