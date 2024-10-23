from django.shortcuts import render

from django.http import HttpResponse


def main_index(request):
    return render(request, 'main_index.html')

def cv_view(request):
    return render(request, 'cv.html')
    
def articles_view(request):
    return render(request, 'articles.html')