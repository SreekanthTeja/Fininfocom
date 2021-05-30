from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse,JsonResponse
import uuid
from django.forms import modelformset_factory

from django.contrib.auth import get_user_model

User = get_user_model()
def studentportfolio(request):
    # EducationFormSet = modelformset_factory(Education, form=EducationForm, exclude=('user', ), extra=1,can_delete=True)
    if request.method == 'POST' and request.is_ajax():
        form1, form2, form3 = UserForm(request.POST), ProfileForm(request.POST, request.FILES), EducationForm(request.POST)
        print(form1.is_valid(), form2.is_valid(), form3.is_valid())
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            # print(form1.changed_data["image"])
            for i in form2:
                print(i,end='\n')
            user = form1.save(commit=False)
            user.username = uuid.uuid4()
            user.save()
            profile = form2.save(commit=False)
            profile.user=user
            profile.save()
            # for i in form3:
            #     print('PRINTER       ', i)
            #     education = i.save(commit=False)
            #     education.user = user
            #     education.save()
            education = form3.save(commit=False)
            education.user = user
            education.save()
            print('redirecting...')
            return redirect("/")
            # return JsonResponse({'message':'Sucessfully uploaded'})
        # print(form1.errors, end="\n\n")
        # print(form2.errors, end="\n\n")
        # print(form3.errors, end="\n\n")
        # print(form3)
        return render(request, 'education.html',{'user':form1,'profile':form2,'education':form3})
    user, profile, education = UserForm(), ProfileForm(), EducationForm()
    return render(request, 'student_details.html', {'user':user,'profile':profile,'education':education})


def addform(request):
    EducationFormSet = modelformset_factory(Education, form=EducationForm, fields=('course','college','year','percentage'), extra=1, can_delete=True)
    return render(request, "details.html", {'form': EducationFormSet()})