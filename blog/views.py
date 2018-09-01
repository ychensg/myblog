from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.
def Home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})
 
def Test(request):
    return render(request,'test.html',{'current_time': datetime.now()})
 
def Detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})
