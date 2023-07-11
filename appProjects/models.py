from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    #owner=
    title = models.CharField(max_length=200)
                                    #db      #django
    description = models.TextField(null=True,blank=True)

    #featured_image
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')

    demi_link = models.CharField(max_length=1000, null=True,blank=True)
    source_link = models.CharField(max_length=100, null=True,blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)

    #relationship to tags  model
    tags = models.ManyToManyField('Tag', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,
                         editable=False)

    def __str__(self):
        return self.title
    
    #cut from single-project.html
    # <!-- <img style="width: 500px;" src="{{ project.featured_image.url }}" alt=""> -->
    @property
    def imageURL(self):
        try:
            img = self.featured_image.url
        except:
            img = ''
        return img





class Review(models.Model):
    #creating a tupple(dropdown where users will choose their vote type)
    VOTE_TYPE = (
        ('up', 'up'),
        ('down', 'down')
    )
    #owner
                                        #on_delete= SETNULL-Wont delete child class when parent class is deleted on contrary to what CASCADE does
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                null=True, blank=True) #related_name='reviews'
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50,choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,
                         editable=False)

    def __str__(self):
        return self.value
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,
                         editable=False)
    
    def __str__(self):
        return self.name
    