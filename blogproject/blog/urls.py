from django.urls import path,include
from blog import views as v


urlpatterns = [
    # 获取文章列表
    path('getArticleList/', v.getArticleList),
    # 获取文章详情
    path('getArticleDetail/', v.getArticleDetail),
    # 获取所有的标签
    path('getTagList/', v.getTagList),
    # 获取标签详情
    path('getTagDetail/',v.getTagDetail),
    # 获取种类的详情
    path('getCategoryDetail/', v.getCategoryDetail),
    # 获取旋转狂详情
    path('getCarrouselList/', v.getCarrouselList),

]