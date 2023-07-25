from rest_framework.pagination import PageNumberPagination


class Pager(PageNumberPagination):
    page_size = 10  # 每页的条数
    # page_query_param = "page"  # 查询的key关键字
    # page_size_query_param = "size" # 不指定默认为 page 和 page_size
    max_page_size = 100   # 每页最大的显示条数

    def get_page_size(self, request):
        page_size = request.query_params.get("page_size")
        if page_size:
            return int(page_size)
        return self.page_size
