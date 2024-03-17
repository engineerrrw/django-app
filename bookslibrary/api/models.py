from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    birth_year = models.SmallIntegerField(null=True, blank=True)
    death_year = models.SmallIntegerField(null=True, blank=True)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'books_author'
    
class BookLanguage(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=4)

    class Meta:
        db_table = 'books_language'

class BookShelf(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'books_bookshelf'

class BookSubject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'books_subject'

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ManyToManyField(Author, through='BookAuthor', related_name='books')
    download_count = models.IntegerField(null=True, blank=True)
    gutenberg_id = models.IntegerField(null=True, blank=True)
    media_type = models.CharField(max_length=16)
    title = models.CharField(max_length=1024)
    language = models.ManyToManyField(BookLanguage,through='BookBookLanguage')
    subjects = models.ManyToManyField(BookSubject, through='BookBookSubject')
    shelfs = models.ManyToManyField(BookShelf, through='BookBookShelves')

    class Meta:
        db_table = 'books_book'

class BookAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_authors')

    class Meta:
        db_table = 'books_book_authors'


class BookBookShelves(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    bookshelf = models.ForeignKey(BookShelf, on_delete=models.CASCADE, related_name='bookbookshelves')

    class Meta:
        db_table = 'books_book_bookshelves'

class BookBookLanguage(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    language = models.ForeignKey(BookLanguage, on_delete=models.CASCADE, related_name='book_book_languages')

    class Meta:
        db_table = 'books_book_languages'

class BookBookSubject(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    subject = models.ForeignKey(BookSubject, on_delete=models.CASCADE, related_name='bookbooksubjects')

    class Meta:
        db_table = 'books_book_subjects'

class BookFormat(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='bookformats')
    mime_type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)

    class Meta:
        db_table = 'books_format'





