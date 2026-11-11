from django.urls import path 
from . import views
app_name = 'books'
urlpatterns = [ path('', views.index, name='index'), path('index2/int:val1/', views.index2), path('int:bookId/', views.viewbook),
path('books/', views.list_books, name='list_books'),
path('books/one/', views.view_one_book, name='view_one_book'),
path('aboutus/', views.aboutus, name='aboutus'),
path('html5/links', views.links, name='links'),
path('html5/text/formatting', views.formatting, name='formatting'),
path('html5/listing', views.listing, name='listing'),
path('html5/tables', views.tables, name='tables'),
]