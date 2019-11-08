from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SPUSpecification, SPU
from apps.meiduo_admin.serializers.specs import SPUSpecificationSerializer, SPUSerializer
from apps.meiduo_admin.utils import PageNum


class SpecView(ModelViewSet):
    serializer_class = SPUSpecificationSerializer
    queryset = SPUSpecification.objects.all()
    pagination_class = PageNum


    def simple(self,request):

        data = SPU.objects.all()
        ser = SPUSerializer(data,many=True)

        return Response(ser.data)