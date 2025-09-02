from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,login,logout

from .models import *
from .forms import *

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Handle invalid login
            pass
    return render(request, 'backend/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = CustomUserModel.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
    return render(request, 'backend/signup.html')
def home_view(request,user_id=None):

    if user_id:
        user_profile = get_object_or_404(CustomUserModel, id=user_id)
    else:
        user_profile = CustomUserModel.objects.order_by('-id').first()
    skills = skillModel.objects.filter(user=user_profile)
    projects = projectModel.objects.filter(user=user_profile).order_by('-created_at')

    # Split track_user into a list for each project
    for project in projects:
        project.tech_list = [t.strip() for t in (project.track_user or "").split(",")]
    experiences = experienceModel.objects.filter(user=user_profile)
    educations = educationModel.objects.filter(user=user_profile).order_by('-start_date')
    project_count = projects.filter(user=user_profile).count()
    technology=skillModel.objects.filter(user=user_profile).count()
    form = ContactForm(request.POST or None)
    
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your message!")  # <-- correct
            return redirect('home')

    context = {
        'user_profile': user_profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
        'user': user_profile,
        'project_count': project_count,
        'technology': technology,
        'form': form
    }

    return render(request, 'frontend/index.html', context)
def resume_view(request):
    user_profile = CustomUserModel.objects.order_by('-id').first()
    skills = skillModel.objects.filter(user=user_profile)
    projects = projectModel.objects.filter(user=user_profile)
    experiences = experienceModel.objects.filter(user=user_profile)
    educations = educationModel.objects.filter(user=user_profile).order_by('-start_date')

    # Split track_user into a list for each project
    for project in projects:
        project.tech_list = [t.strip() for t in (project.track_user or "").split(",")]

    context = {
        'user_profile': user_profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'educations': educations
    }
    return render(request, 'frontend/resume.html', context)
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.fullname = f"{form.cleaned_data.get('first_name', '')} {form.cleaned_data.get('last_name', '')}"
            user_obj.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'backend/editprofile.html', {'form': form})
def profile(request):
    user = request.user
    return render(request, 'backend/profile.html', {'user': user})
def addproject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'backend/addproject.html', {'form': form})

def editproject(request,id):
    project = projectModel.objects.get(id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'backend/addproject.html', {'form': form})
def deleteproject(request,id):
    project = projectModel.objects.get(id=id)
    project.delete()
    return redirect('project_list')
def addskill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'backend/addskill.html', {'form': form})
def editskill(request,id):
    skill = skillModel.objects.get(id=id)
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'backend/addskill.html', {'form': form})
def deleteskill(request,id):
    skill = skillModel.objects.get(id=id).delete()
    return redirect('skill_list')

def addeducation(request):
    if request.method == 'POST':
        form = EducationForm(request.POST, request.FILES)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            return redirect('education_list')
    else:
        form = EducationForm()
    return render(request, 'backend/addeducation.html', {'form': form})
def editeducation(request,id):
    education = educationModel.objects.get(id=id)
    if request.method == 'POST':
        form = EducationForm(request.POST, request.FILES, instance=education)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            return redirect('education_list')
    else:
        form = EducationForm(instance=education)
    return render(request, 'backend/addeducation.html', {'form': form})
def deleteeducation(request,id):
    education = educationModel.objects.get(id=id).delete()
    return redirect('education_list')

def addexperience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect('experience_list')
    else:
        form = ExperienceForm()
    return render(request, 'backend/addexperience.html', {'form': form})
def editexperience(request,id):
    experience = experienceModel.objects.get(id=id)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES, instance=experience)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect('experience_list')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'backend/addexperience.html', {'form': form})
def deleteexperience(request, id):
    experience = experienceModel.objects.get(id=id)
    experience.delete()
    return redirect('dashboard')

def dashboard_view(request):
    return render(request, 'backend/index.html')

def contact_list(request):
    contacts = contactModel.objects.all()
    return render(request, 'backend/contact_list.html', {'contacts': contacts})
def skill_list(request):
    skills = skillModel.objects.all()
    return render(request, 'backend/skill_list.html', {'skills': skills})
def project_list(request):
    projects = projectModel.objects.all()
    return render(request, 'backend/project_list.html', {'projects': projects})
def experience_list(request):
    experiences = experienceModel.objects.all()
    return render(request, 'backend/experience_list.html', {'experiences': experiences})
def education_list(request):
    educations = educationModel.objects.all()
    return render(request, 'backend/education_list.html', {'educations': educations})