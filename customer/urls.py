from django.urls import path
from.views import addcartv,cartshowview,cartdeleteview,checkoutview


urlpatterns = [
     path('add_to_cart/<int:iid>/',addcartv.as_view(), name='addcart'),
     path('casrtshow',cartshowview.as_view(),name='cartshow'),
     path('cartdelete/<int:id>',cartdeleteview,name='delcart'),
     path('checkoutt/<int:cid>',checkoutview.as_view(),name="ckout"),
]
