from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


def jwt_response_payload_handler(token, user, request):

    return {
        'id':user.id,
        'username':user.username,
        'token':token
    }

class PageNum(PageNumberPagination):
    page_size_query_param = 'pagesize'

    max_page_size = 8


    # 重写分页返回结果方法
    def get_paginated_response(self, data):
        return Response(
            {
                'counts':self.page.paginator.count,
                'lists':data,
                'page':self.page.number,
                'pages':self.page.paginator.num_pages,
                'pagesize':self.max_page_size
            }
        )