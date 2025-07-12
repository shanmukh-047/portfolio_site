from django.shortcuts import render

# Homepage
def home(request):
    return render(request, 'portfolio/home.html')

# Optional index page
def index(request):
    return render(request, 'portfolio/index.html')

# About page
def about(request):
    return render(request, 'portfolio/about.html')

# Projects page
def projects(request):
    return render(request, 'portfolio/projects.html')

# Resume page
def resume(request):
    return render(request, 'portfolio/resume.html')  # this page must exist in templates/portfolio/

# Contact page
def contact(request):
    return render(request, 'portfolio/contact.html')

# Contact form handling (POST logic)
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print("Received name:", name)
    return render(request, 'portfolio/contact.html')  # corrected: add 'portfolio/' path
from django.http import FileResponse
import os
from django.conf import settings

def download_resume(request):
    resume_path = os.path.join(settings.BASE_DIR, 'portfolio/static/resume/resume.pdf')
    return FileResponse(open(resume_path, 'rb'), content_type='application/pdf')