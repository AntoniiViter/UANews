from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import NewsForm, CommentForm
from .models import News, Comments
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
        allnews = News.objects.order_by('-created').filter(datearchived__isnull=True)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(allnews, 9)  # 6 employees per page

        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)

        return render(request, 'news/home.html', {'allnews': allnews, 'page_obj': page_obj})


def signupuser(request):
    if request.method=='GET':
        return render(request, 'news/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentnews')
            except IntegrityError:
                return render(request, 'news/signupuser.html', {'form': UserCreationForm(), 'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'news/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})

def loginuser(request):
    if request.method=='GET':
        return render(request, 'news/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'news/loginuser.html', {'form': AuthenticationForm(), 'error': "Username and password didn't match"})
        else:
            login(request, user)
            return redirect('currentnews')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def createnews(request):
    if request.method=='GET':
        return render(request, 'news/createnews.html', {'form': NewsForm()})
    else:
        try:
            form = NewsForm(request.POST, request.FILES)
            newnews = form.save(commit=False)
            newnews.newscreator = request.user
            newnews.save()
            return redirect('currentnews')
        except ValueError:
            return render(request, 'news/createnews.html', {'form': NewsForm(), 'error': 'Передано неправильні дані. Повторіть спробу'})

@login_required
def currentnews(request):
    news = News.objects.order_by('-created').filter(newscreator=request.user, datearchived__isnull=True)
    return render(request, 'news/currentnews.html', {'news': news})

@login_required
def viewnews(request, news_id):
    viewnewss = get_object_or_404(News, pk=news_id, newscreator=request.user)
    if request.method == 'GET':
        form = NewsForm(instance=viewnewss)
        return render(request, 'news/viewnews.html', {'viewnews': viewnewss, 'form': form})
    else:
        try:
            form = NewsForm(request.POST, request.FILES, instance=viewnewss)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'news/createnews.html', {'form': NewsForm(), 'error': 'Передано неправильні дані. Повторіть спробу'})

def archivenews(request, news_id):
    archivenews = get_object_or_404(News, pk=news_id, newscreator=request.user)
    if request.method == 'POST':
        archivenews.datearchived = timezone.now()
        archivenews.save()
        return redirect('currentnews')

def dearchivenews(request, news_id):
    dearchivenews = get_object_or_404(News, pk=news_id, newscreator=request.user)
    if request.method == 'POST':
        dearchivenews.datearchived = None
        dearchivenews.save()
        return redirect('currentnews')

def deletenews(request, news_id):
    deletednews = get_object_or_404(News, pk=news_id, newscreator=request.user)
    if request.method == 'POST':
        deletednews.delete()
        return redirect('currentnews')

def deletenews_archives(request, news_id):
    deletednews = get_object_or_404(News, pk=news_id, newscreator=request.user)
    if request.method == 'POST':
        deletednews.delete()
        return redirect('archivednews')

@login_required
def archivednews(request):
    archivednews = News.objects.filter(newscreator=request.user, datearchived__isnull=False).order_by('-datearchived')
    return render(request, 'news/archivednews.html', {'news': archivednews})

def detail(request, news_id):
    detailnews = get_object_or_404(News, pk=news_id)
    comments = Comments.objects.filter(commentlocation_id=news_id)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(comments, 5)  # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        return render(request, 'news/detail.html', {'comments': comments, 'detailnews': detailnews, 'form': CommentForm(), 'page_obj': page_obj})
    else:
        try:
            form = CommentForm(request.POST)
            newcomment = form.save(commit=False)
            newcomment.commentlocation = detailnews
            newcomment.author = request.user
            newcomment.save()
            return redirect('detail', news_id)
        except ValueError:
            return render(request, 'news/detail.html', {'detailnews': detailnews, 'form': CommentForm(), 'comments': comments, 'page_obj': page_obj, 'error': 'Передано неправильні дані. Повторіть спробу'})
