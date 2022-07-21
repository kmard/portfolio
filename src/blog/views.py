from django.shortcuts import render, get_object_or_404
from blog.models import blog_model

# Create your views here.
def all_blogs(request):

    # blogs = blog_model.objects.order_by('-date')[:5]
    blogs = blog_model.objects.order_by('-date')

    return render(request,'blog/all_blogs.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(blog_model,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})
