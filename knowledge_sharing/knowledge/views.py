import datetime

from django.db.models.functions import ExtractMonth
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, F, Count
from django.views.generic.base import View
from .models import Knowledge
from .forms import AddKnowledgeForm
from .utils.pagination import Pagination


def knowledge_add(request):
    if request.method == 'GET':
        form = AddKnowledgeForm()
        return render(request, 'knowledge_add.html', {'form': form})
    else:
        form = AddKnowledgeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/knowledge/list/')
        else:
            return render(request, 'knowledge_add.html', {'form': form})


def knowledge_detail(request, knowledge_id):
    knowledge = get_object_or_404(Knowledge, id=knowledge_id)
    prev_knowledge = Knowledge.objects.filter(id__lt=knowledge_id).last()
    next_knowledge = Knowledge.objects.filter(id__gt=knowledge_id).first()
    context = {
        'knowledge': knowledge,
        'prev_knowledge': prev_knowledge,
        'next_knowledge': next_knowledge,
    }
    return render(request, 'knowledge_detail.html', context)


def knowledge_list(request):
    search_data = request.GET.get('q', "")
    queryset = Knowledge.objects.filter(Q(content__contains=search_data)|Q(login__startswith=search_data)|Q(bucket__startswith=search_data)|Q(title__contains=search_data)).order_by("-create_time")
    page_object = Pagination(request, queryset, page_size=50)
    context = {
        'search_data': search_data,
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
    }
    return render(request, 'knowledge_list.html', context)


def chart_list(request):
    highlight_queryset = Knowledge.objects.filter(Q(highlight=True)&Q(approved=True))
    most_frequent = Knowledge.objects.filter(approved=True).values('login').annotate(count=Count('id')).order_by('-count').first()

    context = {
        'highlight_queryset': highlight_queryset,
        'most_frequent': most_frequent,
    }

    return render(request, 'chart_list.html', context)


def chart_bar_yearly(request):

    db_data_list = []

    queryset = Knowledge.objects.filter(Q(create_time__year=datetime.datetime.now().year)&Q(approved=True)).values('bucket').annotate(count=Count('id')).order_by('-count')
    d = dict(Knowledge.BUCKET)
    for result in queryset:
        db_data_list.append({
            'name': d[result['bucket']],
            'value': result['count'],
        })

    result = {
        'status': True,
        'data': db_data_list
    }

    return JsonResponse(result)


def chart_bar_monthly(request):

    db_data_list = []

    queryset = Knowledge.objects.filter(Q(create_time__month=datetime.datetime.now().month)&Q(approved=True)).values('bucket').annotate(count=Count('id')).order_by('-count')
    d = dict(Knowledge.BUCKET)
    for result in queryset:
        db_data_list.append({
            'name': d[result['bucket']],
            'value': result['count'],
        })

    result = {
        'status': True,
        'data': db_data_list
    }

    return JsonResponse(result)


def chart_line(request):

    queryset = Knowledge.objects.filter(Q(create_time__year=datetime.datetime.now().year)&Q(approved=True)).annotate(month=ExtractMonth('create_time')).values('month').annotate(count=Count('create_time'))

    legend = [f"{datetime.datetime.now().year}年", ]
    series_list = [
        {
            "name": f'{datetime.datetime.now().year}年',
            "type": 'line',
            "stack": 'Total',
            "data": [_['count'] for _ in queryset]
        },
    ]
    x_axis = [f"{_['month']}月" for _ in queryset]

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)
