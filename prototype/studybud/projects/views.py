from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm



#projectObj = Project.objects



def projects(req):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(req, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project':projectObj})

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm() 

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES) # somethign about sending the picture
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project) # object that is trnsfered into template and every field of this project is outputed

    if request.method == 'POST': # the view is called again when post method created by submit button in htmls form
        
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
   
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object' : project}
    return render(request, 'projects/delete_template.html', context)