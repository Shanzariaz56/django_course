from django_filters import rest_framework as filters
from .models import *


class JobFilter(filters.FilterSet):
    class Meta:
        model = Job
        fields = ['education', 'jobtype', 'experience']