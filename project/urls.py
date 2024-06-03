from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('add/', views.Add, name='add'),
    path('edit/', views.Edit, name='edit'),
    path('update/<int:id>/', views.Update, name='update'),
    path('delete/<int:id>/', views.Delete, name='delete'),
    path('book-service/', views.book_service, name='book_service'),
    
    
    

]
