from django.shortcuts import render,get_object_or_404,get_list_or_404
from blog.models import Post

# Create your views here.


def blog_home(request):
    posts=Post.objects.filter(status=1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid,status=1)

    post.counted_views += 1
    post.save()

    context = {'post': post}

    return render(request, 'blog/blog-single.html', context)

def test(request,pid):
     post=get_list_or_404(Post,id=pid)
     context={'post':post}
     return render(request,'test.html',context)