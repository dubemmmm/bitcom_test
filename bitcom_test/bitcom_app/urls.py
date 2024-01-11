from django.urls import path
from . import views
urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('polling/', views.view_polling_units, name='polling'),
    path('polling_unit/<int:uniqueid>/', views.polling_unit_results, name='polling_unit_results'),
    path('lgas/', views.lga_list, name='lga_list'),
    path('lga_results/<int:pk>/', views.lga_results, name='lga_results'),
    path('new_polling_unit_results/', views.new_polling_unit_results, name='new_polling_unit_results'),
    path('success_page/<int:pk>/', views.success_page, name='success_page'),
    
]
    