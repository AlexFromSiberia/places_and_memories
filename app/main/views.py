from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Memory
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView
# from .forms import TopicForm, EntryForm
from django.http import Http404


def index(request):
    """Welcome page"""
    return render(request, 'main/index.html')


class Places(ListView):
    """Users page with a list of all their memories"""
    model = Memory
    template_name = 'main/list_entry.html'
    # все данные по умолчанию находятся в переменной "object_list" (использовать её в template.py)
    # переопределить имя переменной "object_list" чтобы в template использовать переменную 'news' если нам так УДОБНЕЕ.
    context_object_name = "memories"
    # несуществующие страницы(в списке такого значения нет) будут показаны как 404
    allow_empty = False


class Memories(DetailView):
    model = Memory
    template_name = 'main/detail_entry.html'
    context_object_name = "place"
    allow_empty = False


class MemoryUpdate(SuccessMessageMixin, UpdateView, PermissionRequiredMixin, ):
    """Page: Update memory (for memory owner only)"""
    model = Memory
    template_name = 'main/detail_entry.html'
    context_object_name = "place"
    allow_empty = False



    template_name = 'news/update_an_article.html'
    form_class = AddArticleForm
    success_url = reverse_lazy("news_index")
    permission_required = 'news.can_delete_news_article'
    success_message = 'Article has been successfully updated!'


class ArticleDelete(SuccessMessageMixin, DeleteView, PermissionRequiredMixin):
    """Page: Delete article (for stuff only)"""
    model = NewsArticles
    success_url = reverse_lazy("news_index")
    template_name = 'news/article_delete.html'
    permission_required = 'news.can_delete_news_article'
    success_message = 'Article has been successfully deleted!'