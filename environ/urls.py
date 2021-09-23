from django.urls import path
from environ.views import EnvironView, api_view


app_name = "environ"


urlpatterns = [
    path("", EnvironView.as_view(), name="env"),
    path("openapi/", api_view, name="openapi"),
]
