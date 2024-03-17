from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'

class BookLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookLanguage
        fields = ['code']

class BookSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookSubject
        fields = ['name']

class BookShelfSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookShelf
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    language = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    shelfs = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['title','download_count','author','language','subjects','shelfs']
        depth = 1

    def get_language(self, instance):
        language = instance.language.all()
        if language:
            return BookLanguageSerializer(language, many=True).data
        else:
            return None

    def get_subjects(self, instance):
        subjects = instance.subjects.all()
        if subjects:
            return BookSubjectSerializer(subjects, many=True).data
        else:
            return []

    def get_shelfs(self, instance):
        shelfs = instance.shelfs.all()
        if shelfs:
            return BookShelfSerializer(shelfs, many=True).data
        else:
            return []


