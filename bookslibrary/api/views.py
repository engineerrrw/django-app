from django.shortcuts import render
from rest_framework.response import Response
from .models import Author,Book
from rest_framework.exceptions import *
from .serializers import BookSerializer
from rest_framework.views import APIView
from django.db.models import Q
import json

class AllBooksView(APIView):

    def get(self, request):
        if request.method == 'GET':
            data = request.GET
            author_name = data.get('author_name')
            language_codes = data.get('language_code', '').split(',')
            book_title = data.get('book_title')
            book_id = data.get('book_id')
            mime_type = data.get('mime_type')
            topic = data.get('topic','').split(',')
            filter_query = Q()

            if author_name:
                q1 = Q(author__name__icontains=author_name)
                filter_query &= q1
            
            if language_codes:
                # Filter books by language codes
                q2 = Q()
                for code in language_codes:
                    q2 |= Q(bookbooklanguage__language__code=code)
                filter_query &= q2
            
            if book_title:
                q3 = Q(title__icontains=book_title)
                filter_query &= q3

            if book_id:
                q4 = Q(id=book_id)
                filter_query &= q4

            if mime_type:
                q5 = Q(bookformats__mime_type__icontains=mime_type)
                filter_query &= q5

            if topic:
                for sub_shelf in topic:
                    q6 = Q(bookbookshelves__bookshelf__name__icontains=sub_shelf) | Q(bookbooksubject__subject__name__icontains=sub_shelf)
                filter_query &= q6
            
            books_data = Book.objects.filter(filter_query)
            serializer = BookSerializer(books_data, many=True)
            serialized_data = json.dumps(serializer.data)
            data = json.loads(serialized_data)
            count_of_books = len(data)
            count_dict = {"total_books_count": count_of_books}
            data.insert(0, count_dict)
            return Response(data)

            
            