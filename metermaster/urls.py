from django.urls import path,include
from . import views

app_name = 'metermaster'
urlpatterns = [
    path('/', views.home , name = "home"),
    path('/metermaster_update_form/<int:pk>', views.updatemeterForm , name = 'updateMeterForm'),
    path('/metermaster_delete_form/<int:pk>', views.deletemeterForm , name = 'deleteMeterForm'),
]
