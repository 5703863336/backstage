from rest_framework import serializers

from apps.goods.models import SKU
from apps.orders.models import OrderInfo, OrderGoods

class SKUSerialzier(serializers.ModelSerializer):

    class Meta:
        model = SKU
        fields = ('name','default_image')



class OrderGoodsSerialzier(serializers.ModelSerializer):

    sku = SKUSerialzier()

    class Meta:
        model = OrderGoods
        fields = ('count','price','sku')

class OrderInfoSerialzier(serializers.ModelSerializer):

    skus = OrderGoodsSerialzier(many=True)

    class Meta:
        model = OrderInfo
        fields = '__all__'