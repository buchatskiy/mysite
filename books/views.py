# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book


def search(request):
    error=''
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error='Введите поисковый запрос.'
        elif len(q)>20:
            error='Введите не более 20 символов.'
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('template/search_results.html', {'books': books, 'query': q})
    return render_to_response('template/search_form.html', {'error': error})
