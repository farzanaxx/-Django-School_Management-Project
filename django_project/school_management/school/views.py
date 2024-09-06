from django.shortcuts import render, redirect

from .models import School
from .forms import Schoolform


def school_list(request, ):
    school = School.objects.all()
    return render(request, 'school_info.html', {'school': school})


def scl_info(request):
    if request.method == 'POST':
        forms = Schoolform(request.POST)
        print(forms.is_valid())
        if forms.is_valid():
            forms.save()
            return redirect('school_list')
    else:
        forms = Schoolform()
        return render(request, 'scl_info.html', {'forms': forms})


def scl_update(request, id, ):
    school = School.objects.get(pk=id,)
    if request.method == 'POST':
        forms = Schoolform(request.POST, instance=school)
        if forms.is_valid():
            forms.save()
            return redirect('scl_info')
    else:
        forms = Schoolform(instance=school)
        return render(request, 'scl_info.html', {'forms': forms})


def scl_delete(request,id):
    school = School.objects.get(pk=id,)

    school.delete()
    return redirect("scl_info")
