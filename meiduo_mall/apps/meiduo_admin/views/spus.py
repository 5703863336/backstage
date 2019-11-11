from fdfs_client.client import Fdfs_client
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SPU, Brand, GoodsCategory
from apps.meiduo_admin.utils import PageNum
from apps.meiduo_admin.serializers.spus import SPUSerializer, BrandSerializer, GoodsCategorySerializer


class SPUView(ModelViewSet):

    serializer_class = SPUSerializer
    queryset = SPU.objects.all()
    pagination_class = PageNum

    def brands(self,request):

        data = Brand.objects.all()

        ser = BrandSerializer(data, many=True)

        return Response(ser.data)
    def channel(self, request):

        data = GoodsCategory.objects.filter(parent=None)

        ser = GoodsCategorySerializer(data, many=True)
        return Response(ser.data)


    def channel2(self, request, pk):

        data = GoodsCategory.objects.filter(parent=pk)

        ser = GoodsCategorySerializer(data, many=True)
        return Response(ser.data)

    def images(self,request):

        image = request.data.get('image')
        client = Fdfs_client('utils/fastdfs/client.conf')
        res = client.upload_appender_by_buffer(image.read())
        if res['Status'] != 'Upload successed.':
            return Response({"error":"上传失败"},status=400)
        path = res.get('Remote file_id')
        image_url = 'http://192.168.203.130:8888/'+path
        return Response({'img_url':image_url})