from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from apps.meiduo_admin.views import images
from apps.meiduo_admin.views import options
from apps.meiduo_admin.views import specs
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
]

router = DefaultRouter()
router.register('goods/specs',specs.SpecView,base_name='specs')
router.register('specs/options',options.SpecificationOptionView,base_name='options')
router.register('skus/images',images.SKUImageView,base_name='images')

urlpatterns += router.urls

