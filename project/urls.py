
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
     path('resume/', resume_view, name='resume'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('addskill/', addskill, name='add_skill'),
    path('addproject/', addproject, name='add_project'),
    path('addexperience/', addexperience, name='add_experience'),
    path('addeducation/', addeducation, name='add_education'),
    path('editskill/<int:id>', editskill, name='edit_skill'),
    path('editproject/<int:id>', editproject, name='edit_project'),


    path('deleteexperience/<int:id>', deleteexperience, name='delete_experience'),
    path('deleteeducation/<int:id>', deleteeducation, name='delete_education'),
    path('deleteskill/<int:id>', deleteskill, name='delete_skill'),
    path('deleteproject/<int:id>', deleteproject, name='delete_project'),


    path('editexperience/<int:id>', editexperience, name='edit_experience'),
    path('editeducation/<int:id>', editeducation, name='edit_education'),
    path('profile/', profile, name='profile'),
    path('editprofile/', profile_view, name='editprofile'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('projects/', project_list, name='project_list'),
    path('skills/', skill_list, name='skill_list'),
    path('experiences/', experience_list, name='experience_list'),
    path('educations/', education_list, name='education_list'),
    path('contacts/', contact_list, name='contact_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
