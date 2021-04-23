from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import TodoModel
from .forms import UpdateForm

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class HomeView(ListView):
    model = TodoModel
    template_name = 'index.html'


def create_todo(request):
    if request.method == 'POST':
        todo = request.POST.get('post')
        obj = TodoModel(value = todo)
        obj.save()
        messages.success(request, 'Todo Item Added')
        return redirect('/')

class TodoUpdateView(SuccessMessageMixin, UpdateView):
    model = TodoModel
    form_class = UpdateForm
    success_url = '/'
    template_name = 'update.html'
    success_message = 'Item Updated'
    


class TodoDeleteView(DeleteView):
    model = TodoModel
    template_name = 'delete.html'
    success_url = '/'
    
    def delete(self, request, *args, **kwargs):
        messages.error(self.request, 'Item Deleted')
        return super().delete(request, *args, **kwargs)