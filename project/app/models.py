from django.db import models
from datetime import *
from django.contrib.auth.models import User
#from django.contrib.gis.db import models as gismodels
#from django.contrib.gis.geos import point
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class JobType(models.TextChoices):
    permanent="permanent"
    secondary="secondary"
    internship="internship"

class Education(models.TextChoices):
    bachelor="bachelor"
    master="master"
    phd="phd"

class Industry(models.TextChoices):
    Bussiness="Bussiness"
    Banking="Banking"
    IT="Information Technology"
    Education="Education/traning"
    Telecommunication="Telecommunication"
    Others="Others"

class Experience(models.TextChoices):
    No_experience="NO_Experience"
    One_Year="One_Year"
    Two_years="Two_Years"
    Three_Years_plus="Three_Years_Plus"

def return_date_time():
    now=datetime.now()
    return now +  timedelta(days=10)
 
class Job(models.Model):
    title=models.CharField(max_length=50, null=True)
    description=models.CharField(max_length=200,null=True)
    email=models.EmailField(null=True)
    address=models.CharField(max_length=100,null=True)
    jobtype=models.CharField(max_length=100,
            choices=JobType.choices,
            default=JobType.permanent                    
    )
    education=models.CharField(max_length=100,
            choices=Education.choices,
            default=Education.bachelor                    
    )
    industry=models.CharField(max_length=100,
            choices=Industry.choices,
            default=Industry.Bussiness                     
    )
    experience=models.CharField(max_length=100,
            choices=Experience.choices,
            default=Experience.No_experience                      
    )
    salary = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000000)
        ]
    )
    position=models.IntegerField(default=1)
    company=models.CharField(max_length=100 , null=True)
    #point=gismodels.PointField(default=point(0.0,0.0)) 
    lastdate=models.DateTimeField(default=return_date_time)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    creatAt=models.DateTimeField(auto_now_add=True )

