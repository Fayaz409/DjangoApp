from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('filters',views.builtInFiltersDemo, name='builtInFiltersDemo'),
    path('test_static/', views.TestStaticFiles, name='TestStaticFiles'),
]