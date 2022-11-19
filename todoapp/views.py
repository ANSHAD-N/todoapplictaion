from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from . models import Task
from . forms import TaskForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    content_object_name = 'task'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvindex')

#
# def index(request):
#     task = Task.objects.all()
#     if request.method == 'POST':
#         name = request.POST.get('task', '')
#         priority = request.POST.get('priority', '')
#         date = request.POST.get('date', '')
#         task = Task(name=name, priority=priority, date=date)
#         task.save()
#     return render(request, 'index.html', {'task': task})


def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = TaskForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html', {'f': f, 'task': task})
