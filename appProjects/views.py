from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Project

from .forms import ProjectForm
# Create your views here.

# projectsList = [
#     {
#         'id': '1',
#         'title': 'Ecommerce Website',
#         'description': 'Fully functional ecommerce website',
#         'rated':True
#     },
#     {
#         'id': '2',
#         'title': 'Portfolio Website',
#         'description': 'A personal website to write articles and display work',
#         'rated':False
#     },
#     {
#         'id': '3',
#         'title': 'Social Network',
#         'description': 'An open source project built by the community',
#         'rated':True
#     }
# ]




def funcOne(request):
    # return HttpResponse('This is our project page')

    #render html template files
    # name = 'Happy Otieno Blackie'
    # age = 25;
    # context = {'name':name, 'age':age}
    # context = {'projects':projectsList}

    #ORM
    project = Project.objects.all()
    # print('PROJECT:', project)
    context = {'projects':project}

    return render(request, 'projects/projects.html', context)




#read
def funcTwo(request, pk):
    # return HttpResponse('Quering database: ' + str(pk))
    # projectObject = None
    # for index in projectsList:
    #     if index['id'] == str(pk):
    #         projectObject= index 
    projectObj = Project.objects.get(id=pk)
    # return render(request, 'projects/single-project.html',{'project':projectObj})
    tags = projectObj.tags.all()#one to many
    #reviews = projectObj.reviews.all() # relevant when related_name='reviews' is set in models.py..it will still work
    reviews = projectObj.review_set.all() #many to many
    context = {'project':projectObj, 'tags':tags, 'reviews':reviews}

    return render(request, 'projects/single-project.html',context)


#create project
def  createProject(request):
    form = ProjectForm

    if request.method == 'POST':
        # print('FORM DATA:', request.POST)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form':form}
    return render(request, 'projects/project-form.html', context)


#update project
def updateProject(request, pk):
    # context ={}
    project =Project.objects.get(id=pk)
                        #this will prefill the oroject to be edited
    form = ProjectForm(instance=project)
    # template =  'projects/project-form.html'

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    # context = ['form']=form
                            # template
    return render(request, 'projects/project-form.html', context)


#delete project
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    
    return render(request, 'projects/delete.html', {'object':project})



