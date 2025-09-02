from django import forms
from .models import * 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = [
            'first_name', 'last_name', 'phone','title','date_of_birth','bio','about_description','profile_image','resume_file', 'location','linkedin_url', 'github_url', 'twitter_url', 'instagram_url',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Professional Title'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Short Bio'}),
            'about_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Detailed About'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'LinkedIn URL'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'GitHub URL'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Twitter URL'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Instagram URL'}),
        }



class ProjectForm(forms.ModelForm):
    class Meta:
        model = projectModel
        fields = [
            'title',
            'track_user',
            'description',
            'image',
            'project_url',
            'git_hub_url',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'track_user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Track User'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Project Description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'project_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Project URL'}),
            'git_hub_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'GitHub URL'}),
        }
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = experienceModel
        fields = [
            'job_title',
            'company_name',
            'location',
            'start_date',
            'end_date',
            'description',
        ]

        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Job Description'}),
        }
class EducationForm(forms.ModelForm):
    class Meta:
        model = educationModel
        fields = [
            'degree',
            'institution',
            'field_of_study',
            'location',
            'start_date',
            'end_date',
            'description',
        ]

        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Degree'}),
            'institution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Institution'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Field of Study'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
        }
class SkillForm(forms.ModelForm):
    class Meta:
        model = skillModel
        fields = [
            'skill_name',
            'level',
            'image'
        ]

        widgets = {
            'skill_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Skill Name'}),
            'level': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = contactModel
        fields = ['name', 'phone', 'email', 'message']

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your Message'}))
