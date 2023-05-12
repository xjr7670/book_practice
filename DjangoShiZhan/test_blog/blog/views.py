from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import auth
from django.views.generic import DetailView, ListView

from . import models, forms
from comments.forms import CommentForm

def test_ckeditor_front(request):
    user_obj = models.Loguser.objects.all().first()
    auth.login(request, user_obj)
    blog = models.Blog.objects.get(id=1)
    return render(request, 'blog/test_ckeditor_front.html', {'blog': blog})


def registe(request):
    if request.method == 'POST':
        form_obj = forms.RegForm(request.POST, request.FILES)
        if form_obj.is_valid():
            form_obj.cleaned_data.pop('repassword')
            user_obj = models.Loguser.objects.create_user(**form_obj.cleaned_data,
                                                          is_staff=1,
                                                          is_superuser=1)
            auth.login(request, user_obj)
            return redirect('/')
        else:
            return render(request, 'blog/registe.html', {'formobj': form_obj})

    form_obj = forms.RegForm()
    return render(request, 'blog/registe.html', {'formobj': form_obj})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = auth.authenticate(username=username, password=pwd)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            errormsg = 'Username or password error!'
            return render(request, 'blog/login.html', {'error': errormsg})
    return render(request, 'blog/login.html')


class BlogDetailView(DetailView):
    model = models.Blog
    template_name = 'blog/detail.html'
    context_object_name = 'blog'
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        blog = super(BlogDetailView, self).get_object(queryset=None)
        blog.increase_views()
        return blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


class CategoryView(ListView):
    models = models.Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        cate = get_object_or_404(models.Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(categoty=cate).order_by('-created_time')


class TagView(ListView):
    models = models.Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        tag = get_object_or_404(models.Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag).order_by('creatd_time')


def archives(request, year, month):
    blog_list = models.Blog.objects.filter(
        created_time__year=year,
        created_time__month=month
    ).order_by('-created_time')

    return render(request, 'blog/index.html', context={'blog_list': blog_list})


class MyIndex(ListView):
    model = models.Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        loguser = get_object_or_404(models.Loguser, pk=self.kwargs.get('loguserid'))
        return super(MyIndex, self).get_queryset().filter(author=loguser).order_by('-created_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MyIndex, self).get_context_data(**kwargs)
        context['tabname'] = 'mytab'
        return context


def logout(request):
    auth.logout(request)
    return redirect('/')


class IndexView(ListView):
    model = models.Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog_list'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        pageobj = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        show_pagenumber = 7
        page_date = self.get_page_data(is_paginated, paginator, pageobj, show_pagenumber)
        context.update(page_date)
        context['tabname'] = 'firsttab'
        return context

    def get_page_data(self, is_pageinated, paginator, pageobj, show_pagenumber):
        if not is_pageinated:
            return {}

        left = []
        right = []
        cur_page = pageobj.number
        total = paginator.num_pages
        half = show_pagenumber // 2
        for i in range(cur_page - half, cur_page):
            if i >= 1:
                left.append(i)

        for i in range(cur_page+1, cur_page+half+1):
            if i <= total:
                right.append(i)

        page_data = {
            'left': left,
            'right': right,
        }

        return page_data


class AuthorIndex(ListView):
    model = models.Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        user = get_object_or_404(models.Loguser, pk=self.kwargs.get('id'))
        return super(AuthorIndex, self).get_queryset().filter(author=user).order_by('-created_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorIndex, self).get_context_data(**kwargs)
        context['tabname'] = 'firstatb'
        return context
