from django.urls import path
from . import views

app_name = 'knowledge'

urlpatterns = [

    path('', views.chart_list),

    path('knowledge/list/', views.knowledge_list),
    path('knowledge/add/', views.knowledge_add),
    path('knowledge/detail/<int:knowledge_id>/', views.knowledge_detail),

    path('chart/list/', views.chart_list),
    path('chart/bar_yearly/', views.chart_bar_yearly),
    path('chart/bar_monthly/', views.chart_bar_monthly),
    path('chart/line/', views.chart_line),

]
