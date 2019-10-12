from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect


def login(request):
    if request.user.is_anonymous:
        return render(request, 'members/login.html')
    else:
        return redirect('meeting_list')
