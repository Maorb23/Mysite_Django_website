from django.shortcuts import render
from django.shortcuts import get_object_or_404

def article_view(request):
    return render(request, 'articles/article_home.html')

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/article_detail.html', {'article': article})