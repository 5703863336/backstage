from rest_framework.viewsets import ModelViewSet

from apps.goods.models import Brand
from apps.meiduo_admin.serializers.brands import Brandserilizer
from apps.meiduo_admin.utils import PageNum


class BrandsView(ModelViewSet):


    serializer_class = Brandserilizer
    queryset = Brand.objects.all()
    pagination_class = PageNum