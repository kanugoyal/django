from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
   

]

"""urlpatterns = [
    path("<str:name>", views.index, name="index"),
   

]"""