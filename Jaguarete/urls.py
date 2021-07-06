""" Jaguarete URL Configuration urls """
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import eCommerce.views

app_name = 'jaguarete'
urlpatterns = [
                  path('', eCommerce.views.index, name='Home'),
                  path('about', eCommerce.views.about),
                  path('admin/', admin.site.urls),
                  path('details/<int:id>', eCommerce.views.details, name='details'),
                  path('mod/details/<int:id>', eCommerce.views.detailsmod, name='detailsmod'),
                  path('create', eCommerce.views.ProductCreateView.as_view(template_name='moderador/Create.html')),
                  path('update/<int:id>', eCommerce.views.update, name='update'),
                  path('delete/<int:id>', eCommerce.views.delete, name='delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
