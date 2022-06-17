from django.urls import URLPattern, path
from .import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("home/", views.home,name="home"),
    path("diagnosis/", views.diagnosis,name="diagnosis"),
    path("about/",views.about,name="about"),
    path("explore/", views.explore,name="explore"),
    path("signup/",views.signup,name="signup"),
    path("redrot/",views.redrot,name="redrot"),
    path("smut/", views.smut,name="smut"),
    path("rust/", views.rust,name="rust"),
    path("pineapple/", views.pineapple,name="pineapple"),
    path("wilt/", views.wilt,name="wilt"),
    path("pokkah/", views.pokkah,name="pokkah"),
    path("ratoon/", views.ratoon,name="ratoon"),
    path("scald/",views.scald,name="scald"),
    path("signin/",views.signin,name="signin"),
    path("sign_in_admin/", views.sign_in_admin,name="sign_in_admin")
    ]
    