import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.books.models import Book, Rating
from apps.users.models import CustomUser


class UploadBooksView(APIView):
    def post(self, request):
        with open("dataset/books.csv", "r", encoding="utf-8") as file:
            data = list(csv.reader(file, delimiter=";"))
            bulk_books = []
            for row in data[1:]:
                obj = {
                    "id": row[0],
                    "title": row[1] if row[1] else None,
                    "author": row[2] if row[2] else None,
                    "year_publication": row[3] if row[3] else None,
                    "publisher": row[4] if row[4] else None,
                    "image_1": row[5] if row[5] else None,
                    "image_2": row[6] if row[6] else None,
                    "image_3": row[7] if row[7] else None,
                }
                bulk_books.append(Book(**obj))
            Book.objects.bulk_create(bulk_books)

        return Response(status=status.HTTP_201_CREATED)


class UploadUsersView(APIView):
    def post(self, request):
        with open("dataset/users.csv", "r", encoding="utf-8") as file:
            data = list(csv.reader(file, delimiter=";"))
            bulk_users = []
            for row in data[1:]:
                obj = {
                    "id": row[0],
                    "location": row[1] if row[1] else None,
                    "age": row[2] if row[2] else None,
                }
                bulk_users.append(CustomUser(**obj))
            CustomUser.objects.bulk_create(bulk_users)
        return Response(status=status.HTTP_201_CREATED)


class UploadRatingView(APIView):
    def post(self, request):
        with open("dataset/ratings.csv", "r", encoding="utf-8") as file:
            data = list(csv.reader(file, delimiter=";"))
            bulk_rating = []

            for index, row in enumerate(data[1:]):
                # Solo 40000 registros se cargarán
                if index < 40000:
                    obj = {
                        "user_id": row[0],
                        "book_id": row[1] if row[1] else None,
                        "rating": int(row[2]) if row[2] else None,
                    }
                    qs_books = Book.objects.filter(id=row[1]).exists()
                    qs_users = CustomUser.objects.filter(id=row[0]).exists()
                    if qs_books and qs_users:
                        bulk_rating.append(Rating(**obj))
            Rating.objects.bulk_create(bulk_rating)
        return Response(status=status.HTTP_201_CREATED)
