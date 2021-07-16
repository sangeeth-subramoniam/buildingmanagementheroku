from django.urls import path,include
from . import views

app_name = 'codemaster'
urlpatterns = [
    path('', views.home , name = "home"),
    path('codemaster_update_form/<int:pk>', views.updateCodeForm , name = 'updateCodeForm'),
    path('codemaster_delete_form/<int:pk>', views.deleteCodeForm , name = 'deleteCodeForm'),
]
