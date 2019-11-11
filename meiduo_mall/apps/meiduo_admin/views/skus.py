from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SKU, GoodsCategory, SPU
from apps.meiduo_admin.utils import PageNum
from apps.meiduo_admin.serializers.skus import SKUSerializer, GoodsCategorySerializer
from apps.meiduo_admin.serializers.skus import SPUSpecificationSerializer


class SKUView(ModelViewSet):
    """
        list:
            获取sku
        create:
            保存sku
    """
    # 指定序列化器
    serializer_class = SKUSerializer
    # 指定查询集
    # queryset = SKU.objects.all()
    # 指定分页器
    pagination_class = PageNum

    # 重写get_queryset
    def get_queryset(self):
        # 根据keyword参数返回不同查询集结果
        keyword = self.request.query_params.get('keyword')

        if keyword == '' or keyword is None:
            # 返回所有数据
            return SKU.objects.all()
        else:
            # 返回查询数据
            return SKU.objects.filter(name__contains=keyword)

    # 获取三级分类的业务
    def simple(self, request):
        # 查询分类表获取三级分类
        data = GoodsCategory.objects.filter(subs=None)
        # 返回三级分类信息
        ser = GoodsCategorySerializer(data, many=True)
        return Response(ser.data)

    # 获取商品规格
    def specs(self, request, pk):
        """

        :param request:
        :param pk:  spu商品id
        :return:
        """
        # 1、根据spuid查询spu对象
        spu = SPU.objects.get(id=pk)
        # 2、根据spu获取规格信息
        specs = spu.specs.all()
        # 3、返回规格信息
        ser = SPUSpecificationSerializer(specs, many=True)

        return Response(ser.data)
