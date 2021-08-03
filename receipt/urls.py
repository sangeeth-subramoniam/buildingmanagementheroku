from django.urls import path,include
from . import views

app_name = 'receipt'
urlpatterns = [
    path('', views.home , name = "home"),
    #path('adjustment_update_form/<int:pk>', views.updateadjustmentForm , name = 'updateadjustmentForm'),
    #path('adjustment_delete_form/<int:pk>', views.deleteadjustmentForm , name = 'deleteadjustmentForm'),
]
