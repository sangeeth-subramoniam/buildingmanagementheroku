from django.urls import path,include
from . import views

app_name = 'setpositionmaster'
urlpatterns = [
    path('', views.home , name = "home"),
    path('setpositionmaster_update_form/<int:pk>', views.updatesetpositionForm , name = 'updateSetPositionForm'),
    path('setpositionmaster_delete_form/<int:pk>', views.deletesetpositionForm , name = 'deleteSetPositionForm'),
]
