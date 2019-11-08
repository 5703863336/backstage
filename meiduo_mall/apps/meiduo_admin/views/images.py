from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SKUImage, SKU
from apps.meiduo_admin.serializers.images import SKUImageSerializer, SKUSerializer
from apps.meiduo_admin.utils import PageNum


class SKUImageView(ModelViewSet):

    serializer_class = SKUImageSerializer
    queryset = SKUImage.objects.all()

    pagination_class = PageNum

    def simple(self,request):

        data = SKU.objects.all()

        ser = SKUSerializer(data,many=True)

        return Response(ser.data)
