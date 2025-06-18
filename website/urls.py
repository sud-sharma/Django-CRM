from django.urls import path
from . import views  # Import your views from the current directory

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('register/', views.register_user, name='register'),
    path('record/<int:record_id>', views.customer_record, name='record'),
    # path('record/<int:record_id>/edit', views.edit_record, name='edit_record'),
    path('record/<int:record_id>/delete', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('edit_record/<int:record_id>/', views.update_record, name='edit_record'),
]
