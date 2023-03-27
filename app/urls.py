from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm
from django.contrib import admin
# app_name = 'app'

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("category-title/<val>",
         views.CategoryTitle.as_view(), name="category-title"),
    path("product-detail/<int:pk>",
         views.ProductDetail.as_view(), name="product-detail"),
    path("product/<int:pk>",
         views.ProductView.as_view(), name="product"),
    path("profile/",  views.ProfileView.as_view(),  name="profile"),
    path("address/",  views.address,  name="address"),
    path("updateaddress/<int:pk>",
         views.updateAddress.as_view(), name='update_address'),

    path('add-to-cart/', views.add_to_cart, name="add-to-cart"),
    path('cart/', views.show_cart, name="showcart"),

    path('orders/', views.orders, name='orders'),
    path('search/', views.search, name='search'),
    path('checkout/', views.checkout.as_view(), name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),

    # implementing rest frame work
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetails.as_view(), name='product_detail'),
    path('customers/', CustomerList.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer_detail'),
    path('carts/', CartList.as_view(), name='cart_list'),
    path('carts/<int:pk>/', CartDetail.as_view(), name='cart_detail'),
    path('orders/', OrderPlacedList.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderPlacedDetail.as_view(), name='order_detail'),

    # login authtentication
    path("registration/", views.CustomerRegistrationView.as_view(),
         name="customerregistration"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name='app/login.html',
         authentication_form=LoginForm), name='login'),
    path("passwordchange/", auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',
                                                                 form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(
        template_name="app/passwordchangedone.html"), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    # password reset url
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',
         form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confrim.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html'), name='password_reset_complete'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "EasyBuy"
admin.site.site_title = "Easy Dairy"
admin.site.site_index_title = "Welcome to EsayBuy Online SuperMarket"
