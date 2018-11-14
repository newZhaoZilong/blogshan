from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django import conf

from django.http import JsonResponse

from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from blog.models import Article, Category, Tag
import re

@require_http_methods(['GET'])
def getIndex(request):
    return render(request, 'blog/index.html')


@require_http_methods(['GET'])
def getDetail(request):
    return render(request, 'blog/detail.html')


# @csrf_exempt装饰器能避免'django.middleware.csrf.CsrfViewMiddleware'的检测
# 这里写一个装饰器,用于优化,因为post请求的装饰器都是相同的,返回的错误信息也相同，所以在wrapper里进行了错误捕捉
def easyPost(func):
    @csrf_exempt
    @require_http_methods(['POST'])
    def wrapper(request):
        try:
            return JsonResponse({'code': 0, 'msg': 'success', 'result': func(request)})
        except Exception as e:
            return JsonResponse({'code': 1, 'msg': '%s %sfail!' % (request.path.replace('/', ' ').strip(), e)})

    return wrapper


# 获取文章列表
@easyPost
def getArticleList(request):
    postData = request.POST

    query_set = Article.objects.select_related('category').order_by('-update_date')

    if postData.get('category_id'):
        category_id = postData.get('category_id')
        query_set = query_set.filter(category__id=category_id)
    elif postData.get('tag_id'):
        tag_id = postData.get('tag_id')
        query_set = query_set.prefetch_related('tags').filter(tags__id=tag_id)
        pass

    article_list = []
    isSearch = postData.get('search')
    if isSearch:
        search_reg = re.compile(isSearch)

    # 听说用iterator能节省一些内存
    for article in query_set:
        if isSearch:
            # 如果是search,就判断搜索内容存不存在，如果不存在，就判断下一个
            if not(search_reg.search(article.markdown_body) or search_reg.search(article.title)):
                continue
        article_list.append({
            'title': article.title,
            'summary': article.summary,
            'update_date': article.update_date.strftime('%Y-%m-%d'),
            'category': article.category.name,
            'imgUrl': article.img.url,
            'article_id': article.id,
            'category_id':article.category.id,
            'read_times':article.read_times
        })

    return article_list


# 获取文章详情
@easyPost
def getArticleDetail(request):
    # get后的结果就只是一个对象,tags是manager类型
    article_detail = Article.objects.select_related('category').prefetch_related('tags').get(id = request.POST['article_id'])

    article_length = Article.objects.count()

    next_id = 1 if (article_detail.id + 1 > article_length) else article_detail.id+1

    # 获取,only结果还是queryset,是可遍历的，遍历的结果是tag
    # tag_list = list(article_detail.tags.objects.extra(select={'tag_id': 'id'}).values('name', 'tag_id'))

    tag_list = [{'name':x.name,'tag_id':x.id} for x in article_detail.tags.all()]
    article_detail.read_times += 1
    article_detail.save()
    return {
        'article_id':article_detail.id,
        'title':article_detail.title,
        'html_body':article_detail.html_body,
        'toc':article_detail.toc,
        'category':article_detail.category.name,
        'category_id':article_detail.category.id,
        'update_date':article_detail.update_date.strftime('%Y-%m-%d'),
        'tags':tag_list,
        'next_id':next_id,
        'next_title':Article.objects.get(id = next_id).title,
        'read_times':article_detail.read_times
    }

# 获取所有tag
@easyPost
def getTagList(request):
    # 起别名
    return list(Tag.objects.extra(select={'tag_id':'id'}).values('name','tag_id'))


# 获取标签详情
@easyPost
def getTagDetail(request):
    return Tag.objects.values('name','tag_desc').get(id=request.POST['tag_id'])


# 获取种类详情
@easyPost
def getCategoryDetail(request):
    return Category.objects.values('name', 'category_desc').get(id=request.POST['category_id'])


# 获取旋转框列表kai rou sou
@easyPost
def getCarrouselList(request):

    return {}