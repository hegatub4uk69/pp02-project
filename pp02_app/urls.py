from django.urls import path
from . import views

urlpatterns = [
    path('get-masters-data', views.get_masters_data),
    path('add-order', views.add_order),
    path('update-machine', views.update_machine),
    path('delete-detail', views.del_detail)
]