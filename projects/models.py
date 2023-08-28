from django.db import models
import uuid
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total =models.IntegerField(default=0, null=True, blank=True)
    vote_ratio =models.IntegerField(default=0, null=True, blank=True)
    created =models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False, 
                            primary_key=True)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
    ('up', 'Up Vote'),
    ('down', 'Down Vote')
    )
    # owner = ""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created =models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False, 
                            primary_key=True)


    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created =models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False, 
                            primary_key=True)
    
    def __str__(self):
        return self.name
    
class Business(models.Model):
    name=models.CharField(max_length=200, null=False, blank=False)
    description=models.CharField(max_length=500)
    longitude=models.FloatField()
    latitude=models.FloatField()
    opening_hour=models.CharField(max_length=10)
    closing_hours=models.CharField(max_length=10)
    goggle_id=models.CharField(max_length=400)
    created =models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False, 
                            primary_key=True)
    
    def __str__(self):
        return self.name
    