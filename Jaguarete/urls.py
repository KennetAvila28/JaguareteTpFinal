""" Jaguarete URL Configuration urls """
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import eCommerce.views

app_name = 'jaguarete'
urlpatterns = [
<<<<<<< HEAD
                  path('', eCommerce.views.index, name='Home'),
                  path('signin', eCommerce.views.signin),
=======
                  path('', eCommerce.views.index),
>>>>>>> parent of 0e75ea2 (feat:Update and delete pages)
                  path('about', eCommerce.views.about),
                  path('admin/', admin.site.urls),
                  path('<int:id>', eCommerce.views.details, name='details'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
