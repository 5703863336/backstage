from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from apps.meiduo_admin.views import brands
from apps.meiduo_admin.views import images
from apps.meiduo_admin.views import options
from apps.meiduo_admin.views import orders
from apps.meiduo_admin.views import skus
from apps.meiduo_admin.views import specs
from apps.meiduo_admin.views import spus
from apps.meiduo_admin.views import statistical
from apps.meiduo_admin.views import users
from . import views
urlpatterns = [
    # JWT实现登录
    url(r'^authorizations/$', obtain_jwt_token),
    url(r'^statistical/total_count/$', statistical.UserCountView.as_view()),
    url(r'^statistical/day_increment/$', statistical.UserDayCountView.as_view()),
    url(r'^statistical/day_active/$', statistical.UserActiveCountView.as_view()),
    url(r'^statistical/day_orders/$', statistical.UserOrderCountView.as_view()),
    url(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),
    url(r'^statistical/goods_day_views/$', statistical.GoodsDayView.as_view()),
    url(r'^users/$',users.UserView.as_view() ),
    url(r'^goods/simple/$',specs.SpecView.as_view({'get':'simple'}) ),
    url(r'^goods/specs/simple/$',options.SpecificationOptionView.as_view({'get':'simple'}) ),
    url(r'^skus/simple/$', images.SKUImageView.as_view({'get': 'simple'})),
    url(r'goods/specs',specs.SpecView.as_view({'get':'list','post':'create'})),
    url(r'skus/categories/', skus.SKUView.as_view({'get': 'simple'})),
    url(r'goods/(?P<pk>\d+)/specs/', skus.SKUView.as_view({'get': 'specs'})),

    url(r'goods/brands/simple/$',spus.SPUView.as_view({'get':'brands'})),
    url(r'goods/channel/categories/$', spus.SPUView.as_view({'get': 'channel'})),
    url(r'goods/channel/categories/(?P<pk>\d+)/$', spus.SPUView.as_view({'get': 'channel2'})),
    url(r'goods/images/$',spus.SPUView.as_view({'post':'images'}))
]

router = DefaultRouter()
router.register('goods/specs',specs.SpecView,base_name='specs')
router.register('specs/options',options.SpecificationOptionView,base_name='options')
router.register('skus/images',images.SKUImageView,base_name='images')
# sku表路由
router.register('skus', skus.SKUView, base_name='skus')
router.register('goods/brands', brands.BrandsView, base_name='brands')
router.register('goods', spus.SPUView, base_name='goods')

router.register('orders', orders.OrderView, base_name='orders')

urlpatterns += router.urls

