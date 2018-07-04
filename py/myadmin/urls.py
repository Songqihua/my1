"""py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . views import views,userviews,typeviews,goodsviews,orderviews,authviews

urlpatterns = [



    # 后台首页
    url(r'^$', views.index,name='myadmin_index'),

    # 会员管理myadmin_user_add
    url(r'^user/add/$', userviews.add,name='myadmin_user_add'),
    # url(r'^user/insert/$', userviews.insert,name='myadmin_user_insert'),

    url(r'^user/index/$', userviews.index,name='myadmin_user_list'),
    url(r'^user/delete/$', userviews.delete,name='myadmin_user_delete'),
    url(r'^user/edit/$', userviews.edit,name='myadmin_user_edit'),


    # 分类管理
    url(r'^classify/add/$', typeviews.add,name='myadmin_classify_add'),
    url(r'^classify/index/$', typeviews.index,name='myadmin_classify_list'),
    url(r'^classify/delete/$', typeviews.delete,name='myadmin_classify_delete'),
    url(r'^classify/edit/$', typeviews.edit,name='myadmin_classify_edit'),
    # 商品管理
    url(r'^goods/add/$', goodsviews.add,name='myadmin_goods_add'),
    url(r'^goods/index/$', goodsviews.index,name='myadmin_goods_list'),
    url(r'^goods/delete/$', goodsviews.delete,name='myadmin_goods_delete'),
    url(r'^goods/edit/$', goodsviews.edit,name='myadmin_goods_edit'),



    
        #订单管理
    url(r'^orders/list/$',orderviews.list,name='myadmin_orders_list'),

    url(r'^orders/edit/$',orderviews.edit,name='myadmin_orders_edit'),

    url(r'^orders/info/$',orderviews.info,name='myadmin_orders_info'),

 # 后台权限管理
    # 后台登录
    url(r'^login/$',authviews.mylogin,name='myadmin_login'),
    # 退出登录
    url(r'^loginout/$',authviews.mylogout,name='myadmin_loginout'),

    # 后台用户添加
    url(r'^auth/user/add$',authviews.useradd,name='auth_user_add'),
    # 后台用户列表
    url(r'^auth/user/list$',authviews.userlist,name='auth_user_list'),
    url(r'^auth/user/del/(?P<uid>[0-9]+)$',authviews.userdel,name='auth_user_del'),

    # # 后台组添加
    url(r'^auth/group/add$',authviews.groupadd,name='auth_group_add'),
    # # 后台组列表
    url(r'^auth/group/list$',authviews.grouplist,name='auth_group_list'),
    url(r'^auth/group/edit/(?P<gid>[0-9]+)$',authviews.groupedit,name='auth_group_edit'),
    url(r'^auth/group/del/(?P<gid>[0-9]+)$',authviews.groupdel,name='auth_group_del'),




]
