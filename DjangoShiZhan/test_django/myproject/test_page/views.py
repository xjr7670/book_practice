from django.shortcuts import render

from . import models
from utils.paginater import Paginater


def person_page(request):
    cur_page_num = request.GET.get('page')
    total_count = models.Person.objects.all().count()
    one_page_lines = 10
    page_maxtag = 9

    total_page, remainder = divmod(total_count, one_page_lines)
    if remainder:
        total_page += 1

    try:
        cur_page_num = int(cur_page_num)
        if cur_page_num > total_page:
            cur_page_num = total_page
    except Exception as e:
        cur_page_num = 1

    rows_start = (cur_page_num-1) * one_page_lines
    rows_end = cur_page_num * one_page_lines

    if total_page < page_maxtag:
        page_maxtag = total_page

    half_page_maxtag = page_maxtag // 2
    page_start = cur_page_num - half_page_maxtag
    page_end = cur_page_num + half_page_maxtag

    if page_start <= 1:
        page_start = 1
        page_end = page_maxtag

    if page_end >= total_page:
        page_end = total_page
        page_start = total_page - page_maxtag + 1
        if page_start <= 1:
            page_start = 1

    per_list = models.Person.objects.all()[rows_start:rows_end]

    html_page = ['<li><a href="/test_page/person_page/?page=1">Home</a></li>']

    if cur_page_num <= 1:
        html_page.append('<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>')
    else:
        html_page.append(f'<li><a href="/test_page/person_page/?page={cur_page_num-1}><span aira-hidden="true">&laquo;</span></a></li>')

    for i in range(page_start, page_end+1):
        if i == cur_page_num:
            html_temp = f'<li class="active"><a href="/test_page/person_page/?page={i}">{i}</a></li>'
        else:
            html_temp = f'<li><a href="/test_page/person_page/?page={i}">{i}</a></li>'
        html_page.append(html_temp)

    if cur_page_num >= total_page:
        html_page.append('<li class="disabled"><a href="#"><span aira-hidden="true">&raquo;</span></a></li>')
    else:
        html_page.append(f'<li><a href="/test_page/person_page/?page={cur_page_num+1}"><span aria-hidden="true">&raquo;</span></a></li>')

    html_page.append(f'<li><a href="/test_page/person_page/?page={total_page}">Last</a></li>')
    page_nav = "".join(html_page)
    return render(request, 'test_page/list_person.html', {'person_list': per_list, 'page_nav': page_nav})


def person_pagenew(request):
    cur_page_num = request.GET.get('page')
    if not cur_page_num:
        cur_page_num = '1'
    total_count = models.Person.objects.all().count()
    one_page_lines = 6
    page_maxtag = 9
    page_obj = Paginater(url_address='/test_page/person_pagenew/',
                         cur_page_num=cur_page_num,
                         total_rows=total_count,
                         one_page_lines=one_page_lines,
                         page_maxtag=page_maxtag)
    per_list = models.Person.objects.all()[page_obj.data_start:page_obj.data_end]
    return render(request,
                  'test_page/list_person.html',
                  {'person_list': per_list, 'page_nav': page_obj.html_page()})
