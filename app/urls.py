"""multi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from app import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.Pattern1_1.as_view(), name='pattern1_1'),
    url(r'^pattern1_2/$', views.Pattern1_2.as_view(), name='pattern1_2'),
    url(r'^pattern1_3/$', views.Pattern1_3.as_view(), name='pattern1_3'),
    url(r'^pattern2/$', views.Pattern2.as_view(), name='pattern2'),
]
