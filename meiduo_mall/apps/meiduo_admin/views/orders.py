from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.meiduo_admin.serializers.orders import OrderInfoSerialzier
from apps.meiduo_admin.utils import PageNum
from apps.orders.models import OrderInfo


class OrderView(ReadOnlyModelViewSet):

    serializer_class = OrderInfoSerialzier
    pagination_class = PageNum

    def get_queryset(self):

        keyword = self.request.query_params.get('keyword')

        if keyword == '' or keyword is None:

            return OrderInfo.objects.all()
        else:
            return OrderInfo.objects.filter(order_id__contains=keyword)
    @action(methods=['put'],detail=True)
    def status(self, request, pk):
        """

        :param request:
        :param pk: 接受前端传递order——id
        :return:
        """
        # 1、根据id查询订单对象
        try:
            order = OrderInfo.objects.get(order_id=pk)
        except:
            return Response({'error'"订单信息错误"}, status=400)
        # 2、获取订单状态编号
        status = request.data.get('status')
        # 3、修改订单状态
        order.status = status
        order.save()
        # 4、返回订单状态信息
        return Response({'status':status})

