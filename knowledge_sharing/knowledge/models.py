from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
from django.template.loader import render_to_string


class Knowledge(models.Model):

    BUCKET = (
        (0, 'COS'),
        (1, 'Deal Creation'),
        (2, 'Deal Support'),
        (3, 'Merchandising'),
        (4, 'CMBS'),
        (5, 'Instock'),
        (6, 'Ad-hoc'),
        (7, 'AMA'),
    )

    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=16, verbose_name='Login')
    bucket = models.IntegerField(default=0, choices=BUCKET, verbose_name='Bucket')
    title = models.CharField(max_length=100, verbose_name='Title')
    content = RichTextUploadingField(verbose_name='Content')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = 'Knowledge'
        verbose_name_plural = 'Knowledge'

    def __str__(self):
        return self.title


class Sidebar(models.Model):
    # 侧边栏的模型数据

    STATUS = (
        (1, '隐藏'),
        (2, '展示')
    )

    DISPLAY_TYPE = (
        (1, '搜索'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最近评论'),
        (5, '文章归档'),
        (6, 'HTML')
    )

    title = models.CharField(max_length=50, verbose_name="模块名称")  # 模块名称
    display_type = models.PositiveIntegerField(default=1, choices=DISPLAY_TYPE,
                                               verbose_name="展示类型")  # 侧边栏  搜索框/最新文章/热门文章/HTML自定义等
    content = models.CharField(max_length=500, blank=True, default='', verbose_name="内容",
                               help_text="如果设置的不是HTML类型，可为空")  # 这个字段是专门用来给HTML类型用的，其他类型可为空
    sort = models.PositiveIntegerField(default=1, verbose_name="排序", help_text='序号越大越靠前')
    status = models.PositiveIntegerField(default=2, choices=STATUS, verbose_name="状态")  # 隐藏  显示状态
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")  # 时间

    class Meta:
        verbose_name = "侧边栏"
        verbose_name_plural = verbose_name
        ordering = ['-sort']

    def __str__(self):
        return self.title

    @classmethod  # 类方法装饰器，这个就变成了这个类的一个方法可以调用
    def get_sidebar(cls):
        return cls.objects.filter(status=2)  # 查询到所有允许展示的模块

    @property  # 成为一个类属性，调用的时候不需要后边的（）,是只读的，用户没办法修改
    def get_content(self):
        if self.display_type == 1:
            context = {

            }
            return render_to_string('sidebar/search.html', context=context)
        elif self.display_type == 2:
            context = {

            }
            return render_to_string('sidebar/new_post.html', context=context)
        elif self.display_type == 3:
            context = {

            }
            return render_to_string('sidebar/hot_post.html', context=context)
        elif self.display_type == 4:
            context = {

            }
            return render_to_string('sidebar/commment.html', context=context)
        elif self.display_type == 5:  # 文章归档
            context = {

            }
            return render_to_string('sidebar/archives.html', context=context)
        elif self.display_type == 6:  # 自定义侧边栏

            return self.content  # 在侧边栏直接使用这里的html，模板中必须使用safe过滤器去渲染HTML
