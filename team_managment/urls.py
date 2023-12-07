from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('details/<int:pk>', views.Details.as_view(), name='DetailsUpdate'),
    path('create', views.Create.as_view(), name='Create'),
    path('delete/<int:pk>', views.Delete.as_view(), name='Delete'),
]
