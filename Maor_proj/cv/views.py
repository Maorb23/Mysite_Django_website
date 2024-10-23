#Maor_proj/cv/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CVUploadForm
from .models import CV
from django.http import HttpResponse, Http404
import os
from django.conf import settings

def cv_success(request):
    return HttpResponse("CV uploaded successfully.")

def test_view(request):
    return HttpResponse("Test view is working!")

def cv_view(request):
    try:
        cv = CV.objects.last()

        if request.method == 'POST':
            form = CVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(reverse('Maor_proj.cv:cv_view'))
        else:
            form = CVUploadForm()

        context = {
            'form': form,
            'cv': cv
        }
        return render(request, 'cv/cv_template.html', context)
    except Exception as e:
        print("Exception in cv_view:", e)
        import traceback
        traceback.print_exc()
        return HttpResponse("An error occurred.")


def download_cv(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)
    file_path = cv.cv_file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = f'inline; filename={os.path.basename(file_path)}'
            return response
    raise Http404
