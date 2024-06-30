from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_view, name='create_model'),
    path('add-data/<str:model_name>/', views.add_data, name='add_data'),
    path('add-data-page/', views.add_data_page, name='add_data_page'),
    path('show-data/<str:model_name>/', views.show_data, name='show_data'),
    
]
