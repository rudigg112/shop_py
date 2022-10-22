from django.contrib import admin
from django.contrib.auth import views as authViews
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views as userViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('auth/', authViews.LoginView.as_view(template_name='shop/loginuser.html'), name='userlogin'),
    path('auth_ex/', authViews.LogoutView.as_view(template_name='shop/product/list.html')),
    path('register/', userViews.register, name="reg"),
    path('', include('shop.urls', namespace='shop')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
