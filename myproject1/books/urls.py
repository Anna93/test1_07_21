
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'), # go to the home page
    path('librarian-books', views.books, name = 'librarian-books'),  # books page
    path('librarian-history', views.history, name = 'librarian-history') # history page
]
