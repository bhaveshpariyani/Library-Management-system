from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name = "home"),
    path("books",views.books_list,name="books_list"),
    path("add_books",views.add_books,name="add-books"),
    path("show-book/<book_id>",views.show_book,name = "show-book"),
    path("update-book/<book_id>",views.update_book,name = "update-book"),
    path("delete-book/<book_id>",views.delete_book,name = "delete-book"),
    
]
