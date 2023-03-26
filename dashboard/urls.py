from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('bookings/', views.bookings, name='bookings'),
    path('floor_plan/', views.floor_plan, name='floor_plan'),
    path('staffroom/', views.staffroom, name='staffroom'),
    path('contacts/', views.contacts, name='contacts'),
    path('settings/', views.settings, name='settings'),
    path('create_section_table/<int:section_id>/', views.create_section_and_table, name='create_section_and_table'),
    path('create_section_and_table/', views.create_section_and_table, name='create_section_and_table'),
    path('get_calendar_data/', views.get_calendar_data, name='get_calendar_data'),
    path('delete_section/<int:section_id>/', views.delete_section_or_table, name='delete_section'),
    path('delete_table/<int:table_id>/', views.delete_section_or_table, name='delete_table'),
    path('update_table/<int:table_id>/', views.update_table, name='update_table'),
    path('update_section/<int:section_id>/', views.update_section, name='update_section'),
    path('create_booking/', views.create_booking, name='create_booking'),



]
