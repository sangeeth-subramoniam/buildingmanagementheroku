from django.urls import path,include
from . import views

app_name = 'readingarea'
urlpatterns = [
    path('', views.home , name = "home"),
    path('readingarea_update_form/<int:pk>', views.updateReadingForm , name = 'updateReadingForm'),
    path('readingarea_delete_form/<int:pk>', views.deleteReadingForm , name = 'deleteReadingForm'),
]
