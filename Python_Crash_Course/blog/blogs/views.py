from django.shortcuts import render
from .models import BlogPost
from .forms import BlogForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    posts = BlogPost.objects.order_by("-date_added")
    context = {"posts": posts}
    return render(request, 'blogs/index.html', context)

def new_blog(request):
    """新增博文"""
    if request.method != "POST":
        # 未提交数据，显示空表单
        form = BlogForm()
    else:
        # POST提交的数据，进行处理
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

def edit_post(request, post_id):
    """修改博文"""

    post = BlogPost.objects.get(id=post_id)

    if request.method != "POST":
        # 如果是初次请求，即刚打开编辑页面
        form = BlogForm(instance=post)
    else:
        # 如果是已经提交了修改
        form = BlogForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {"post": post, "form": form}
    return render(request, 'blogs/edit_blog.html', context)
