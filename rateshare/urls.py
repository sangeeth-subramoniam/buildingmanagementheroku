from django.urls import path,include
from . import views

app_name = 'rateshare'
urlpatterns = [
    path('', views.home , name = "home"),
    path('rateshare_update_form/<int:pk>', views.updaterateForm , name = 'updateRateForm'),
    path('rateshare_delete_form/<int:pk>', views.deleterateForm , name = 'deleteRateForm'),
    path('ajax/load-stores/', views.load_store, name='ajax_load_stores'),
    path('ajax/load-meters/', views.load_meters, name='ajax_load_meters'),
]


