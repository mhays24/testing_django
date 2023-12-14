from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import School, Membership

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_detail')
    return render(request, 'login.html')

@login_required
def user_detail(request):
    return render(request, 'user_detail.html')

@login_required
def join_school(request):
    if request.method == 'POST':
        code = request.POST['code']
        school = School.objects.filter(code=code).first()
        if school is not None:
            Membership.objects.create(user=request.user, school=school)
            return redirect('school_detail', school_id=school.id)
    return render(request, 'join_school.html')

@login_required
def school_detail(request, school_id=None):
    if request.method == 'POST':
        code = request.POST['code']
        school = School.objects.filter(code=code).first()
        if school is not None:
            Membership.objects.create(user=request.user, school=school)
            return redirect('school_detail', school_id=school.id)
    else:
        school = None
        if school_id is not None:
            school = School.objects.get(id=school_id)
    return render(request, 'school_detail.html', {'school': school})