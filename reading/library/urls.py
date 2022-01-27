from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="library-home"),
    path('<int:id>', views.show, name="library-show"),
    path('new/', views.create, name="library-new")
]
