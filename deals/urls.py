from django.urls import path
from .views import DealsView
from . import views

urlpatterns = [
    path('upload/', DealsView.as_view(), name='file-upload'),
    path('csv_data/', views.DealsListView, name='csv-data'),
]
