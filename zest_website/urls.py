from django.contrib import admin
from django.conf.urls import url
from zest_website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # =============== Urls ================
    url(r'^$', views.home, name="home"),

    # ===============Athentication Urls================
    url(r'^sign-in/$', views.sign_in, name="sign_in"),
    url(r'^sign-up/$', views.sign_up, name="sign_up"),
    url(r'^signed-in/$', views.signed_in, name="signed_in"),
    url(r'^signed-up/$', views.signed_up, name="signed_up"),
    url(r'^reset-password/$', views.reset_password, name="reset_password"),
    url(r'^reset-password-complete/$', views.reset_password_send, name="reset_password_send"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^profile/$', views.profile, name="profile"),


]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
