from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import TodoForms
from .models import Task
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView , DeleteView


# Create your views here.

class TaskListview(ListView):
    model=Task
    template_name='index.html'
    context_object_name ='task1'
    
class TaskDetailsview(DetailView):
    model=Task
    template_name='details.html'
    context_object_name= 'task'    
 
class TaskUpdateview(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='task'
    fields=('name','priority','date')
    
    def get_success_url(self) -> str:
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):     
    model=Task
    template_name='delete.html'
    success_url=reverse_lazy('cbvhome')


def todofun(request):
    taski=Task.objects.all()
    if request.method=='POST':
        name= request.POST.get('name','')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=Task(name=name, priority=priority,date=date)
        task.save()
    return render (request,'index.html',{'task1':taski})

def delete(request,taskid):
    dtask=Task.objects.get(id=taskid)
    if request.method=='POST':
        dtask.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    forms=TodoForms(request.POST or None,instance=task)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'form':forms,'task':task})
    
    