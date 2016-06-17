"""FLstuff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from FL import views

urlpatterns = [
    url(r'^$', views.frontpage, name='frontpage'),
    url(r'^bs_css/$', views.bs_css, name='bs_css'),
    url(r'^bs_comp/$', views.bs_components, name='bs_components'),
    url(r'^bs_theme/$', views.bs_theme, name='bs_theme'),
    url(r'^bs_just/$', views.bs_just, name='bs_justify'),
    url(r'^jq_func/$', views.jq_functions, name='jq_functions'),
    url(r'^jq_hw/$', views.jq_hw, name='jq_homework'),
    url(r'^plugins/$', views.plugins, name='plugins'),
    url(r'^hw2_adv/$', views.hw2_advanced, name='hw2_adv'),
    url(r'^hw2_adv_json/json/$', views.hw2_json, name='hw2_json'),
    url(r'^hw2_adv_json/$', views.hw2_table_json, name='hw2_tbl_json'),
    url(r'^admin/', admin.site.urls),
]
