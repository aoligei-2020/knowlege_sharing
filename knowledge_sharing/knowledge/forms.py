from django import forms
# from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingFormField
from .models import Knowledge


class BootStrap:
    bootstrap_exclude_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段，给每个字段的插件设置
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            # 字段中有属性，保留原来的属性，没有属性，才增加。
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass


class BootStrapForm(BootStrap, forms.Form):
    pass


class AddKnowledgeForm(BootStrapModelForm):

    # BUCKET = (
    #     (0, 'COS'),
    #     (1, 'Deal Creation'),
    #     (2, 'Deal Support'),
    #     (3, 'Merchandising'),
    #     (4, 'CMBS'),
    #     (5, 'Instock'),
    #     (6, 'Ad-hoc'),
    #     (7, 'AMA'),
    # )
    #
    # login = forms.CharField(label='创建者login', max_length=16)
    # bucket = forms.ChoiceField(label='创建者所属Bucket', choices=BUCKET)
    # title = forms.CharField(label='标题', max_length=100)
    # content = RichTextUploadingFormField(label='内容')

    class Meta:
        model = Knowledge
        fields = [
            'login',
            'bucket',
            'title',
            'content',
        ]
