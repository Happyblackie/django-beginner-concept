"""
URL configuration for devsearchlive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

#connecting to media url in settings.py
from django.conf import settings
from django.conf.urls.static import static

# from django.http import HttpResponse


# def funcOne(request):
#     return HttpResponse('This is our project page')

# def funcTwo(Request, pk):
#     return HttpResponse('Quering database: ' + str(pk))

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('projects/', funcOne),
    # path('project/<str:pk>/', funcTwo)
    path('', include('appProjects.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)