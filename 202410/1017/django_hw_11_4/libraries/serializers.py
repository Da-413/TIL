from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):
    review_count = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_reviews(self, object):
        reviews = Review.objects.filter(book=object)
        return ReviewListSerializer(reviews, many=True).data

    def get_review_count(self, object):
        return object.review_set.count()

class ReviewListSerializer(serializers.ModelSerializer):
    class BookIsbnSerializer(serializers.ModelSerializer):
            class Meta:
                model = Book
                fields = ('isbn',)
        
    book = BookIsbnSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('content', 'score', 'book',)
        

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)