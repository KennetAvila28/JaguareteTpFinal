""" Jaguarete URL Configuration urls """
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import eCommerce.views

app_name = 'jaguarete'
urlpatterns = [
                  path('', eCommerce.views.index, name='Home'),
                  path('signin', eCommerce.views.signin),
                  path('signup', eCommerce.views.signup),
                  path('about', eCommerce.views.about),
                  path('admin/', admin.site.urls),
                  path('details/<int:id>', eCommerce.views.details, name='details'),
                  path('mod/details/<int:id>', eCommerce.views.detailsmod, name='detailsmod'),
                  path('create', eCommerce.views.ProductCreateView.as_view(template_name='moderator/Create.html')),
                  path('update/<int:id>', eCommerce.views.update, name='update'),
                  path('delete/<int:id>', eCommerce.views.delete, name='delete'),
                  path('addtocart/<int:id>', eCommerce.views.addtocart, name='addtocart'),
                  path('cart', eCommerce.views.cart, name='cart'),
                  path('removetocart/<int:id>', eCommerce.views.revovetocart, name='removetocart'),
                  path('filtercategory/<int:id>', eCommerce.views.filtercategory, name='filtercategory'),
                  path('logout', eCommerce.views.logOut, name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
