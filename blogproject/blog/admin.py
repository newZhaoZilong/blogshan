from django.contrib import admin
# Register your models here.
from .models import Tag,Article,Category

from blog.mytoc import TocExtension  # 锚点的拓展

import markdown

class ArticleAdmin(admin.ModelAdmin):
    # 用于后台展示
    list_display = ('title','update_date_local',)
    # 重写保存模型的方法，object就是提交的模型对象,要save,新建change是False,修改是true,form.changedata是每次修改的东西
    def save_model(self,request,obj,form,change):
        # img_dirPath = '../static/img/'
        # obj.img_url = img_dirPath+obj.img_url
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(),
        ])
        obj.html_body = md.convert(obj.markdown_body)
        obj.toc = md.toc
        obj.save()

admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Category)
