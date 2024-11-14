from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy

# Create your views here.
# CRUD : Create, Read, Update, Delete 
# List 

# 클래스형 뷰, 함수형 뷰가 있음.
# 사용자는 웹페이지에 접속 한다... ==> (의미) 페이지를 본다
#  - 사용자 : URL을 입력 
#  - 서버 : 웹 서버가 뷰를 찾아서 동작(응답) 시킨다. 
class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']

    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
   