from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic
from django.urls import reverse_lazy
from .models import Blog
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'blogs/create.html'
    model = Blog
    fields = ['author','title', 'text']
    success_url = reverse_lazy('blogs:index')

def ViewPostView(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blogs/view.html', {'blog': blog})

class UpdateView(generic.edit.UpdateView):
    template_name = 'blogs/update.html'
    model = Blog
    fields = ['author','title', 'text']
    success_url = reverse_lazy('blogs:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'blogs/delete.html'
    model = Blog
    success_url = reverse_lazy('blogs:index')

class FilterView(generic.ListView):
    template_name = 'blogs/Filter.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.filter(title__contains='title')

class OrderView(generic.ListView):
    template_name = 'blogs/Order.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.order_by('-published_date')

class FilterOrderView(generic.ListView):
    template_name = 'blogs/FOrder.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.filter(title__icontains='title').order_by('title')