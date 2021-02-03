from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
# Create your views here.
from .models import Blog

def blog_all(request):

    blogs = Blog.objects.order_by('-currentdate')
    return render(request, 'blog_all.html', {'blogs': blogs})



def detail(request, blog_no):

    blog=get_object_or_404(Blog,pk=blog_no)

    return render(request,'detail.html',{'blog':blog})

    return render(request,'detail.html',{'num':blog_no})
