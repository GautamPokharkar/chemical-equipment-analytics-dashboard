from django.urls import path
from .views import upload_csv, download_report

urlpatterns = [
    path("upload/", upload_csv),
    path("report/", download_report),
]
