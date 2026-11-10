from django.urls import path 
from . import views
app_name = 'books'
urlpatterns = [ path('', views.index, name='index'), path('index2/int:val1/', views.index2), path('int:bookId/', views.viewbook),
path('books/', views.list_books, name='list_books'),
path('books/one/', views.view_one_book, name='view_one_book'),
path('aboutus/', views.aboutus, name='aboutus'),
]