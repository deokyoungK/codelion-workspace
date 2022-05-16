from django.contrib import admin
from django.urls import path
import snsapp.views
import accounts.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', snsapp.views.home, name='home'),

    path('createpost/', snsapp.views.createpost, name='createpost'),
    path('detail/<int:post_id>', snsapp.views.detail, name='detail'),
    path('new_comment/<int:post_id>', snsapp.views.new_comment, name='new_comment'),
 
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),

    path('freehome/', snsapp.views.freehome, name='freehome'),
    path('freecreatepost/', snsapp.views.freecreatepost, name='freecreatepost'),
    path('freedetail/<int:post_id>', snsapp.views.freedetail, name='freedetail'),
    path('freenew_comment/<int:post_id>', snsapp.views.freenew_comment, name='freenew_comment'),


]
