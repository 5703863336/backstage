from rest_framework.generics import ListCreateAPIView

from apps.meiduo_admin.serializers.users import UserSerializer
from apps.meiduo_admin.utils import PageNum
from apps.users.models import User


class UserView(ListCreateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.filter(is_staff=False)

    pagination_class = PageNum

    def get_queryset(self):

        keyword = self.request.query_params.get('keyword')

        if keyword == '' or keyword is None:

            return User.objects.filter(is_staff=False)
        else:

            return User.objects.filter(is_staff=False,username__contains=keyword)