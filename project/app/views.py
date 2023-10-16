from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from .filters import *
# Create your views here.

@api_view(['GET'])
def getAllJobs(request):
    
    filterset = JobFilter(request.GET, queryset=Job.objects.all().order_by('id'))
    serializer = jobSerializer(filterset.qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getJobById(request, pk):
    job = get_object_or_404(Job, id=pk)
    serializer = jobSerializer(job, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def newJob(request):
    data = request.data
    job = Job.objects.create(**data)
    serializer = jobSerializer(job, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    job.title = request.data['title']
    job.description = request.data['description']
    job.email = request.data['email']
    job.address = request.data['address']
    job.jobType = request.data['jobType']
    job.education = request.data['education']
    job.industry = request.data['industry']
    job.experience = request.data['experience']
    job.salary = request.data['salary']
    job.positions = request.data['positions']
    job.company = request.data['company']
    job.lastDate = request.data['lastDate']
    job.user = request.data['user']
    job.createdAt = request.data['createdAt']
    job.save()
    serializer = jobSerializer(job, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    serializer = jobSerializer(job, many=False)
    job.delete()
    return Response({'message':'Job is Deleted successfully!'}, status=status.HTTP_200_OK)

    
@api_view(['GET'])
def getTopicStats(request, topic):
    # args = {'title__icontains' : topic}
    # jobs = Job.objects.filter(**args)
    jobs = Job.objects.filter(title__icontains=topic)
    if len(jobs)==0:
        return Response({'message' : 'No stats found for the {topic}'.format(topic=topic)})

    stats = jobs.aggregate(
        total_jobs=Count('title'),
        avg_positions=Avg('positions'),
        avg_salary=Avg('salary'),
        min_salary = Min('salary'),
        max_salary = Min('salary'),
    )
    return Response(stats)

# Create your views here.
