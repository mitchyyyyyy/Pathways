from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from base.forms import InquiryForm
from base.models import Service

class HomeView(View):
    template_name = 'base/home.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

class AboutView(View):
    def get(self, request):
        return render(request, 'base/about.html')

class ContactView(View):
    template_name = 'base/contact.html'

    def get(self, request):

        context = {
            'form': InquiryForm()
        }

        return render(request, self.template_name, context)
    
    def post(self, request):
        form = InquiryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your inquiry has been sent successfully.')
            return redirect("base:contact")
        else:
            messages.error(request, 'Please fill in the required fields.')
            return render(request, self.template_name, {'form': form})

    
class ServicesView(View):
    def get(self, request):
        return render(request, 'base/services.html')

class ServicesDetailView(View):
    template_name = 'base/service-detail.html'
    def get(self, request, slug):
        service = Service.objects.get(slug=slug)
        context = {
            "service": service
        }
        return render(request, self.template_name, context)

class BlogView(View):
    def get(self, request):
        return render(request, 'base/blog.html')

class BlogDetailView(View):
    def get(self, request):
        return render(request, 'base/blog_detail.html')

class TeamView(View):
    def get(self, request):
        return render(request, 'base/team.html')
    
class FAQView(View):
    def get(self, request):
        return render(request, 'base/faq.html')