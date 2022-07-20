from django.shortcuts import render
from blog.models import blog_model

# Create your views here.
def all_blogs(request):

    # blogs = blog_model.objects.order_by('-date')[:5]
    blogs = blog_model.objects.order_by('-date')

    return render(request,'blog/all_blogs.html',{'blogs':blogs})