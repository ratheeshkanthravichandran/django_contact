from django.db import models
from django.shortcuts import redirect, render
from contact.models import Contact
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                 DetailView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView
                                 )


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'index.html'
    context_object_name = 'contacts'
    ordering = ['-id']


class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = 'contact_detail.html'

class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact 
    fields = ['name','phone','city']
    template_name = 'create_contact.html'
    success_url = '/contact/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact 
    fields = ['name','phone','city']
    template_name = 'create_contact.html'
    success_url = '/contact/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'delete_confirm.html'
    success_url = '/contact/'



# Total contact list in admin page

def admin_page(request):
    contacts = Contact.objects.all()

    context ={

        'contacts':contacts

    }
    return render(request, 'super_admin.html', context)