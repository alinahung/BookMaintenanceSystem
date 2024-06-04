"""BookMaintenanceSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

import books.views as bviews
import accounts.views as aviews

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("", bviews.book_search, name="Book"),
    
    # path("add_book/", bviews.add_book),
    path("edit_book/<int:pk>/", bviews.edit_book,name="edit_book"),
    
    path("delete_book/<int:pk>/", bviews.delete_book,name="delete_book"),
    
    path("create_book/", bviews.create_book,name="create_book"),
    
    path("lend_record/<int:pk>/", bviews.lend_record,name="lend_record"),
    
    path("book_detail/<int:pk>/", bviews.book_detail,name="book_detail"),
    
    path("login/", aviews.sign_in,name="Login"),
    path("log_out/", aviews.log_out,name="Logout"),
    path("register/", aviews.register,name="Sign_up"),
    
]
