"""UANews URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from news import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Todos
    path('create/', views.createnews, name='createnews'),
    path('current/', views.currentnews, name='currentnews'),
    path('archives/', views.archivednews, name='archivednews'),
    path('news/<int:news_id>', views.viewnews, name='viewnews'),
    path('news/<int:news_id>/detail', views.detail, name='detail'),
    path('news/<int:news_id>/delete', views.deletenews, name='deletenews'),
    path('news/<int:news_id>/archive', views.archivenews, name='archivenews'),
    path('news/<int:news_id>/dearchive', views.dearchivenews, name='dearchivenews'),
    path('news/<int:news_id>/archives/delete', views.deletenews_archives, name='deletenews_archives'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
