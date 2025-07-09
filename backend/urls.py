from django.contrib import admin
from django.urls import path, include
from tasks.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),  # agora usa sua view
    path('users/', include('users.urls')),  # rotas: /users/register, /users/login, /users/logout
    path('tasks/', include('tasks.urls')),  # rotas: /tasks/...
]
