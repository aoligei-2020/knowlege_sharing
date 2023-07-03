from django.contrib import admin
from .models import Knowledge


# Register your models here.
@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    admin.site.site_title = 'RE知识分享站'
    admin.site.site_header = 'RE知识分享站'
    admin.site.index_title = 'RE知识分享站属性列表'

    list_display = ['id', 'login', 'bucket', 'title', 'create_time']
    search_fields = ['title', 'login', 'bucket']
    list_filter = ['bucket', 'approved', 'highlight']
    date_hierarchy = 'create_time'
    list_per_page = 25
    ordering = ['create_time']

    # autocomplete_fields = ['activity', 'product_family', 'general_ledger', 'non_measurable_type']