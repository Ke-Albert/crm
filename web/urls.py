from django.urls import path
from web.views import customer,payment,account

urlpatterns = [

    path('customer/list/', customer.customer_list),
    path('customer/add/', customer.customer_add),
    path('customer/edit/(?P<cid>\d+)/', customer.customer_edit),
    path('customer/del/(?P<cid>\d+)/', customer.customer_del),
    path('customer/import/', customer.customer_import),
    path('customer/tpl/', customer.customer_tpl),

    path('payment/list/', payment.payment_list),
    path('payment/add/', payment.payment_add),
    path('payment/edit/(?P<pid>\d+)/', payment.payment_edit),
    path('payment/del/(?P<pid>\d+)/', payment.payment_del),

    #login
    path('login/', account.login),
    path('login/out/', account.login_out),

]
