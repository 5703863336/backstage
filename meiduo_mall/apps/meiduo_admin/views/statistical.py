from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from datetime import date, timedelta

from apps.goods.models import GoodsVisitCount
from apps.meiduo_admin.serializers import GoodsSerializer
from apps.users.models import User


class UserCountView(APIView):


    def get(self,request):

        count = User.objects.filter(is_staff=False).count()

        return Response({'count':count})
class UserDayCountView(APIView):

    def get(self,request):
        now_day = date.today()

        count = User.objects.filter(is_staff=False,date_joined__gte=now_day).count()

        return Response({'count':count})
class UserActiveCountView(APIView):

    def get(self,request):

        now_day = date.today()
        count = User.objects.filter(last_login__gte=now_day).count()
        return Response({'count':count})

class UserOrderCountView(APIView):

    def get(self,request):

        now_day = date.today()
        count = User.objects.filter(orderinfo__create_time__gte=now_day).count()
        return Response({'count':count})

class UserMonthCountView(APIView):

    def get(self,request):

        now_day = date.today()

        last_month_day = now_day - timedelta(29)

        everyday_count = []
        for i in range(30):
            index_date = last_month_day + timedelta(i)
            next_date = index_date + timedelta(1)
            rd = set(User.objects.filter(is_staff=False,date_joined__gte=index_date, date_joined__lt=next_date))
            count = len(rd)

            everyday_count.append({
                'count':count,
                'date':index_date
            })
        return Response(everyday_count)

class GoodsDayView(APIView):

    def get(self,request):

        now_day = date.today()

        data = GoodsVisitCount.objects.filter(date__gte=now_day)
        ser = GoodsSerializer(data,many=True)

        return Response(ser.data)


