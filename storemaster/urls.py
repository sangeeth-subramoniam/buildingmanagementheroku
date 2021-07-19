from django.urls import path,include
from . import views

app_name = 'storemaster'
urlpatterns = [
    path('', views.home , name = "home"),
    path('codemaster_update_form/<int:pk>', views.updateStoreForm , name = 'updateStoreForm'),
    path('codemaster_delete_form/<int:pk>', views.deleteStoreForm , name = 'deleteStoreForm'),
]
