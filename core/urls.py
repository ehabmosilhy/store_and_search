from django.contrib import admin
from django.urls import path

from files import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  path('admin/', admin.site.urls),
                  path('files', views.file_list, name='file_list'),
                  path('files/upload', views.upload_file, name='upload_file'),
                  path('search', views.search, name='search'),
                  path('', views.home, name='home')

              ]
urlpatterns += static(settings.FILES_URL, document_root=settings.FILES_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
