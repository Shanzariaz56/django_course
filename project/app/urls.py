from django.urls import path
from .views import *
urlpatterns = [
    path("jobs",getAllJobs),
    path("jobs/<str:pk>",getJobById),
    path("jobs/new",newJob),
    path("jobs/update/<str:pk>",updateJob),
    path("jobs/delete/<str:pk>",deleteJob),
    path("stats/<str:topic>", getTopicStats),
]
