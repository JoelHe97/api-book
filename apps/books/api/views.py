from rest_framework import generics
from ..models import Book
from .serializers import BookSerializer, BookTitleUpdateSerializer, BookDetailSerializer
from utils.pagination import CustomPagination


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.order_by("title")
    serializer_class = BookSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Book.objects.all()
        # Obtiene lo queryparams
        title = self.request.query_params.get("title", None)
        author = self.request.query_params.get("author", None)

        # Filtra el qs si encuentra algún queryparam
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if author is not None:
            queryset = queryset.filter(author__icontains=author)
        return queryset


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BookDetailSerializer
        # Utiliza el serializer personalizado solo cuando sea un metodo PUT
        if self.request.method == "PUT":
            return BookTitleUpdateSerializer
        return BookSerializer
