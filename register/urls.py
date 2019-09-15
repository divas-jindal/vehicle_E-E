from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('', views.registerfacVehicle, name="all"),
    path('veh/',views.veh)
    # path("new/", views.CreateGroup.as_view(), name="create"),
    # path("posts/in/<slug>/",views.SingleGroup.as_view(),name="single"),
    # path("join/<slug>/",views.JoinGroup.as_view(),name="join"),
    # path("leave/<slug>/",views.LeaveGroup.as_view(),name="leave"),
]
