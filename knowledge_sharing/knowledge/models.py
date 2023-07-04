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
    approved = models.BooleanField(null=True, verbose_name='已审核')
    highlight = models.BooleanField(default=False, verbose_name='高亮的')
    content = RichTextUploadingField(verbose_name='Content')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = 'Knowledge'
        verbose_name_plural = 'Knowledge'

    def __str__(self):
        return self.title
