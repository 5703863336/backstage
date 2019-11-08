from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SpecificationOption, SPUSpecification
from apps.meiduo_admin.serializers.options import SpecificationOptionSerializer, OptionSerializer
from apps.meiduo_admin.utils import PageNum


class SpecificationOptionView(ModelViewSet):

    serializer_class = SpecificationOptionSerializer
    queryset = SpecificationOption.objects.all()
    pagination_class =PageNum

    def simple(self,request):

        data = SPUSpecification.objects.all()

        ser = OptionSerializer(data,many=True)

        return Response(ser.data)