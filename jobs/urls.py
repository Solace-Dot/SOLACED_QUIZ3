from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("<int:pk>/", views.job_detail, name="job_detail"),
    path("<int:pk>/update/", views.JobUpdateView.as_view(), name="job_update"),
    path("<int:pk>/delete/", views.JobDeleteView.as_view(), name="job_delete"),
    path("<int:pk>/apply/", views.apply_job, name="apply_job"),
]
