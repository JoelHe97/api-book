import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.books.api.serializers import BookSerializer
from apps.books.rating.api.serializers import RatingSerializer
from apps.users.api.serializers import UserSerializer
from apps.books.models import Book,Rating
from apps.users.models import CustomUser


class UploadBooksView(APIView):
    def post(self, request):
        # Obtén el archivo subido desde la solicitud HTTP
        archivo = request.FILES["books"]

        # Lee y decodifica el contenido del archivo CSV
        archivo_csv = archivo.read().decode('ISO-8859-1')
        # Divide el contenido en líneas
        lineas = archivo_csv.splitlines()

        for index, linea in enumerate(csv.reader(lineas)):
            if index != 0 and index<100:
                column = linea[0].replace("&amp;", "&")
                column = column.replace("&lt;", "<")
                column = column.replace("&gt;", ">")
                column = column.replace("; ", ", ")
                column = column.replace(";:", ":")
                column = column.replace(" ;", " ,")
                column = column.split(";")
                print(index)
                row = {
                    "id": column[0],
                    "title": column[1].replace('"', "") if len(column)>1 else None,
                    "author": column[2].replace('"', "") if len(column)>2 else None,
                    "year_publication": column[3].replace('"', "") if len(column)>3 else None,
                    "publisher": column[4].replace('"', "") if len(column)>4 else None,
                    "image_1": column[5].replace('"', "") if len(column)>5 else None,
                    "image_2": column[6].replace('"', "") if len(column)>6 else None,
                    "image_3": column[7].replace('"', "") if len(column)>7 else None,
                }
                qs_books = Book.objects.filter(id=column[0])
                if not qs_books.exists():
                    serializer = BookSerializer(data=row)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(
                            serializer.errors, status=status.HTTP_400_BAD_REQUEST
                        )
        return Response(status=status.HTTP_201_CREATED)
    
class UploadUsersView(APIView):
    def post(self, request):
        # Obtén el archivo subido desde la solicitud HTTP
        archivo = request.FILES["users"]

        # Lee y decodifica el contenido del archivo CSV
        archivo_csv = archivo.read().decode('ISO-8859-1')
        # Divide el contenido en líneas
        lineas = archivo_csv.splitlines()

        for index, linea in enumerate(csv.reader(lineas)):
            if index != 0:
                if index == 4923:
                    pass
                column = linea[0].replace("&amp;", "&")
                column = column.replace("&lt;", "<")
                column = column.replace("&gt;", ">")
                column = column.replace("; ", ", ")
                column = column.replace(";:", ":")
                column = column.replace(" ;", " ,")
                column = column.split(";")
                row = {
                    "id": column[0],
                    "location": column[1].replace('"', "") if len(column)>1 else None,
                    "age": column[2].replace('"', "") if len(column)>2 else None,
            
                }
                qs_users = CustomUser.objects.filter(id=column[0])
                if not qs_users.exists():
                    serializer = UserSerializer(data=row)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(
                            serializer.errors, status=status.HTTP_400_BAD_REQUEST
                        )
        return Response(status=status.HTTP_201_CREATED)
    
    
class UploadRatingView(APIView):
    def post(self, request):
        # Obtén el archivo subido desde la solicitud HTTP
        archivo = request.FILES["ratings"]

        # Lee y decodifica el contenido del archivo CSV
        archivo_csv = archivo.read().decode('ISO-8859-1')
        # Divide el contenido en líneas
        lineas = archivo_csv.splitlines()

        for index, linea in enumerate(csv.reader(lineas)):
            if index != 0 and index<4968:
                if index == 4923:
                    pass
                column = linea[0]

                column = column.split(";")
                row = {
                    "user": int(column[0].replace('"', "")),
                    "book": column[1].replace('"', "") if len(column)>1 else None,
                    "rating": int(column[2].replace('"', "")) if len(column)>2 else None,
            
                }
                exist_user=CustomUser.objects.filter(id=row["user"]).exists()
                exist_book=Book.objects.filter(id=row["book"]).exists()
                if exist_user and exist_book:
                    serializer = RatingSerializer(data=row)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(
                            serializer.errors, status=status.HTTP_400_BAD_REQUEST
                        )
        return Response(status=status.HTTP_201_CREATED)
