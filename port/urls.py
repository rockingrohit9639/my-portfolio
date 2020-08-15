"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = "Rohit Kumar Saini - Admin"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Edit Contents"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="Home"),
    path('about/', views.about, name="AboutMe"),
    path('blog/', views.blog, name="AboutMe"),
    path('portfolio/', views.portfolio, name="Portfolio"),
    path('blog/<slug:slug>/', views.blogPost, name="blogPost"),
    path('search/', views.search, name="Search"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.handlelogin, name="login"),
    path('logout/', views.handlelogout, name="logout"),
    path('forgotpass/', views.forgotpass, name="Forgot Pass"),
    # APIs for posting comments
    path('postcomment/', views.postcomment, name='PostComment'),
]
