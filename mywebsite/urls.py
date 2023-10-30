from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('record/<int:pk>/edit', views.update_record, name='update_record'),
    path('add_record/', views.add_record, name='add_record'),
]
