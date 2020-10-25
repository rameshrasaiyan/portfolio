from django.shortcuts import render
from projects.models import Project


# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html',  {'projects': projects})


def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/details.html', {'project': project})
