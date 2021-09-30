from django.shortcuts import render
from . models import Blog
from events.models import Event

# Create your views here.


def get_blogs(request):
    blogs = Blog.objects.all()
    events = Event.objects.all()[:2]
    popular_posts = Blog.objects.all()[:3]

    try:
        if request.GET['news'] is not None:
            blog_id = request.GET.get('news')
            context = {'events': events}

            try:
                blog = Blog.objects.get(id=blog_id)
                context['blog'] = blog
                context['title'] = blog.title
                context['popular_posts'] = popular_posts

            except:
                return Blog.DoesNotExist

            return render(request, 'blog/single-blog.html', context)

        elif request.GET['category'] is not None:
            category = request.GET['category']  # blog category
            try:
                blogs = Blog.objects.filter(category=category)

                return render(request, 'blog/blog.html', {'blogs': blogs, 'popular_posts': popular_posts})
            except:
                pass
    except:
        pass

    context = {'blogs': blogs, 'events': events,
               'popular_posts': popular_posts}

    return render(request, 'blog/blog.html', context)
