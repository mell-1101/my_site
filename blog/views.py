from django.shortcuts import render,get_object_or_404,get_list_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.


def blog_home(request):
    posts=Post.objects.filter(status=True,published_date__lte=timezone.now())
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request, pid):
    published_posts = Post.objects.filter(
    status=True,
    published_date__lte=timezone.now()
    ).order_by('id')
    post = get_object_or_404(published_posts, id=pid)
    post.counted_views += 1
    post.save()


    posts = list(published_posts)
    index = posts.index(post)

    previous_post = posts[index - 1] if index > 0 else None
    next_post = posts[index + 1] if index < len(posts) - 1 else None

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }

    return render(request, 'blog/blog-single.html', context)

