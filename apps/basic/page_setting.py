from rest_framework.pagination import PageNumberPagination


class Pager(PageNumberPagination):
    page_size = 30  # 每页的条数
    page_query_param = "page"  # 查询的key关键字
    # 指定一个关键字, 如果前端指定的关键字获取页多少条数据 ，则在这里的page_size的值就会失效
    page_size_query_param = "size"
    # # 每页最大的显示条数
    max_page_size = 100
