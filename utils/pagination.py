from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 100

    # Sobreescribir método para adjuntar n°de páginas en el response
    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data["pages"] = self.page.paginator.num_pages
        return response
