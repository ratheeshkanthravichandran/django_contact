from django.urls import path
from .views import (ContactListView, 
                    ContactDetailView, 
                    ContactCreateView,
                    ContactUpdateView, 
                    ContactDeleteView,
                    admin_page)

urlpatterns = [
    path('admin-page/', admin_page, name='admin-page'),
    path('', ContactListView.as_view(), name='home' ),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail' ),
    path('create/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),


]