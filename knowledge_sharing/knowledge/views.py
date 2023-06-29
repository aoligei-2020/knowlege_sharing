from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, F
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
    page_object = Pagination(request, queryset)
    context = {
        'search_data': search_data,
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
    }
    return render(request, 'knowledge_list.html', context)


def chart_list(request):
    return render(request, 'chart_list.html')


def chart_bar_yearly(request):

    db_data_list = [
        {"value": 15, "name": 'COS'},
        {"value": 20, "name": 'Deal Creation'},
        {"value": 36, "name": 'Deal Support'},
        {"value": 10, "name": 'Merchandising'},
        {"value": 45, "name": 'CMBS'},
        {"value": 66, "name": 'Instock'},
        {"value": 20, "name": 'Ad-hoc'},
        {"value": 50, "name": 'AMA'},
    ]

    result = {
        'status': True,
        'data': db_data_list
    }

    return JsonResponse(result)


def chart_bar_monthly(request):

    db_data_list = [
        {"value": 15, "name": 'COS'},
        {"value": 20, "name": 'Deal Creation'},
        {"value": 36, "name": 'Deal Support'},
        {"value": 10, "name": 'Merchandising'},
        {"value": 45, "name": 'CMBS'},
        {"value": 66, "name": 'Instock'},
        {"value": 20, "name": 'Ad-hoc'},
        {"value": 50, "name": 'AMA'},
    ]

    result = {
        'status': True,
        'data': db_data_list
    }

    return JsonResponse(result)


def chart_line(request):
    legend = ["2023年", ]
    series_list = [
        {
            "name": '2023年',
            "type": 'line',
            "stack": 'Total',
            "data": [15, 20, 36, 10, 10, 10, 45, 10, 66, 40, 20, 50]
        },
    ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)
