from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Postform, Commentform, freePostform, freeCommentform
from .models import Post, freePost


# Create your views here.
def home(request):
    posts = Post.objects.filter().order_by('-date')
    return render(request,'index.html', {'posts':posts})

def createpost(request):
    if request.method == "POST" or request.method == "FILES":
        form = Postform(request.POST, request.FILES)
        if(form.is_valid):
            form.save()
            return redirect('home')
            
    else:
        form = Postform()
    return render(request, 'post_form.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = Commentform() 
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

def new_comment(request, post_id):
    filled_form = Commentform(request.POST) 
    if(filled_form.is_valid):
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('detail', post_id)



def freehome(request):
    posts = freePost.objects.filter().order_by('-date')
    return render(request,'free_index.html', {'posts':posts})

def freecreatepost(request):
    if request.method == "POST" or request.method == "FILES":
        form = freePostform(request.POST, request.FILES)
        if(form.is_valid):
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            return redirect('freehome')
            
    else:
        form = freePostform()
    return render(request, 'free_post_form.html', {'form':form})

def freedetail(request, post_id):
    post_detail = get_object_or_404(freePost, pk=post_id)
    freecomment_form = freeCommentform()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'freecomment_form':freecomment_form})

def freenew_comment(request, post_id):
    filled_form = freeCommentform(request.POST) 
    if(filled_form.is_valid):
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(freePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)


