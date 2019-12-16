from django.shortcuts import render


# Create your views here.
def error_404(request, exception):
    data = {}
    return render(request, 'errors/notfound.html', data)
