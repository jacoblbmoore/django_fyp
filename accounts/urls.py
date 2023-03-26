from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create_section_table/<int:section_id>/', views.create_section_and_table, name='create_section_table'),
    path('create_section_table/', views.create_section_and_table, name='create_section_table'),

]
