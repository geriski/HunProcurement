"""The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

Defines URL patterns for learning_logs."""

from django.urls import path
from notices import views

urlpatterns = [

        # Home page

        path('', views.index, name='index'),
        
        #Notices
        
        path('notices', views.FilteredRegNumberListView.as_view(), name='notices'),
        
        #Stats
        
        path('stats',views.StatRegNumberView.as_view(), name='stats'),
        
        # Import RegNumber

        path('simple_upload', views.index, name='simple_upload'),
        
    ]