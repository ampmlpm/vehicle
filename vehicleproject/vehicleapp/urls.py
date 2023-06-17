from django.urls import path
from . import views
app_name='vehicleapp'
urlpatterns = [

    path('',views.index, name='index'),
    path('vehicle/<int:vehicle_id>/',views.detail,name='detail'),
    path('add/',views.add_vehicle,name='add_vehicle'),
    path('update/<int:id>/', views.update,name='update'),
    path('delete/<int:id>/', views.delete,name='delete')
]