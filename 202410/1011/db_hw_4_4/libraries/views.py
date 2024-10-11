from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    review_form = ReviewForm()
    reviews = book.review_set.all()

    context = {
        'book': book,
        'review_form': review_form,
        'reviews': reviews,
    }
    return render(request, 'libraries/detail.html', context)


def reviews_create(request, pk):
    book = Book.objects.get(pk=pk)
    review_form = ReviewForm(request.POST)

    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.book = book
        review.user = request.user
        review.save()
        return redirect('libraries:detail', book.pk)
    context = {
        'book': book,
        'review_form': review_form,
    }
    return render(request, 'libraries/detail.html', context)


def reviews_delete(request, book_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    book = Book.objects.get(pk=book_pk)
    review.delete()
    return redirect('libraries:detail', book.pk)