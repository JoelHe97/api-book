from django.urls import path
from .views import UploadBooksView,UploadUsersView,UploadRatingView

app_name = "core"

urlpatterns = [
    path("upload/books/", UploadBooksView.as_view()),
    path("upload/users/", UploadUsersView.as_view()),
    path("upload/ratings/", UploadRatingView.as_view()),
]
