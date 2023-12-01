from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('details', views.details, name='Details'),
    path('details/<int:id>', views.details, name='DetailsUpdate'),
    path('delete/<int:id>', views.delete, name='Delete'),
]