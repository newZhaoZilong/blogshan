from django.db import models
import datetime

# Create your models here.


# 文章标签
class Tag(models.Model):
    name = models.CharField('文章标签名称',max_length=20)
    # 这个是标签的唯一标识符，就是标签对外的id
    # slug = models.SlugField(unique=True)
    tag_desc = models.TextField('文章标签描述',max_length=240)
    def __str__(self):
        return self.name

# 分类标签
class Category(models.Model):
    name = models.CharField('文章分类名称',max_length=20)
    # 分类的唯一标识符
    # slug = models.SlugField(unique=True)
    category_desc = models.TextField('文章分类描述',max_length=240)

    def __str__(self):
        return self.name



class Article(models.Model):
    # IMG_LINK = '/static/blog/img/summary.png'
    # 第一个参数就是verbose_name
    title = models.CharField('文章标题',max_length=150,)

    summary = models.TextField('文章摘要')
    # 字数不限,文章内容输入内容为markdown文本，在提交的时候转为html字符串存入数据库
    body = models.TextField('文章内容')
    # 图片名称，在提交的时候添加图片地址存入数据库
    img_url=models.CharField('图片',max_length=255)
    # auto_now_add只会在创建时更新,以后都不会更新
    create_date = models.DateTimeField('创建时间',auto_now_add=True)
    # auto_now每次修改时都会更新时间
    update_date = models.DateTimeField('修改时间',auto_now=True)
    #文章的唯一标识符
    # slug = models.SlugField(unique=True)
    # 文章分类，添加外键后，在后台管理界面可select
    # print('models.CASCADE',models.CASCADE)
    # ,on_delete=models.CASCADE 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项,此参数为了避免两个表里的数据不一致问题
    category = models.ForeignKey(Category,verbose_name="文章分类",on_delete=models.CASCADE)
    # 文章标签
    tags = models.ManyToManyField(Tag,verbose_name='标签')

    toc = models.CharField('导航',max_length=400,editable=False)

    def my_property(self):
        return self.update_date.strftime('%Y-%m-%d %H:%M:%S')
    my_property.short_description = "修改时间"
    # 这个属性用于后台展示
    update_date_local = property(my_property)

    def __str__(self):
        return self.title[:20]






