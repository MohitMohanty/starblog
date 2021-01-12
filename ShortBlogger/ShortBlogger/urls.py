from articles import views as article_views
from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls import url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^articles/',include('articles.urls')),
    url(r'^accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('',article_views.article_list,name="home"),
   
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)