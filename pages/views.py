from .models import Page
from .forms import PageForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy 
# Create your views here.

@method_decorator(login_required, name='dispatch')
class PageListView(ListView):
    model = Page

@method_decorator(login_required, name='dispatch')
class PageDetailView(DetailView):
    model = Page    

@method_decorator(login_required, name='dispatch')
class PageCreate(CreateView):
    model = Page    
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')
    
@method_decorator(login_required, name='dispatch')
class PageUpdate(UpdateView):
     model = Page
     form_class = PageForm
     template_name_suffix = '_update_form'
     success_url = reverse_lazy('pages:pages')
    
     def get_success_url(self):
         return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
     
@method_decorator(login_required, name='dispatch')
class PageDelete(DeleteView):
     model = Page
     success_url = reverse_lazy('pages:pages')

