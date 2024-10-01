from django.shortcuts import render, redirect, get_object_or_404
from .models import Study

def main_view(request):
    studies = Study.objects.all()
    return render(request, 'studies/main_view.html', {'studies': studies})

def add_study(request):
    if request.method == "POST":
        study = Study(
            study_name=request.POST['study_name'],
            study_description=request.POST['study_description'],
            study_phase=request.POST['study_phase'],
            sponsor_name=request.POST['sponsor_name']
        )
        study.save()
        return redirect('main_view')
    return render(request, 'studies/add_study.html')

def edit_study(request, study_id):
    study = get_object_or_404(Study, id=study_id)
    if request.method == "POST":
        study.study_name = request.POST['study_name']
        study.study_description = request.POST['study_description']
        study.study_phase = request.POST['study_phase']
        study.sponsor_name = request.POST['sponsor_name']
        study.save()
        return redirect('main_view')
    return render(request, 'studies/edit_study.html', {'study': study})

def view_study(request, study_id):
    study = get_object_or_404(Study, id=study_id)
    return render(request, 'studies/view_study.html', {'study': study})

def delete_study(request, study_id):
    study = get_object_or_404(Study, id=study_id)
    study.delete()
    return redirect('main_view')
