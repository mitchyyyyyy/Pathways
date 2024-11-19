# create urls for the views
from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('service/<slug:slug>/', views.ServicesDetailView.as_view(), name='service-detail'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<int:id>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('team/', views.TeamView.as_view(), name='team'),
    path('faq/', views.FAQView.as_view(), name='faq'),
]