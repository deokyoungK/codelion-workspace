from django.shortcuts import render, redirect
from .forms import Postform

# Create your views here.
def home(request):
    return render(request,'index.html')

def createpost(request):
    if request.method == "POST" or request.method == "FILES":
        form = Postform(request.POST, request.FILES)
        if(form.is_valid):
            form.save()
            return redirect('home')
            
    else:
        form = Postform()
    return render(request, 'post_form.html', {'form':form})