from django.contrib import admin
from django.urls import path, re_path
from trips.views import home, post_detail, showImg, post_new

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    re_path(r'^post/(?P<pk>\d+)/$', post_detail, name="post_detail"),

    path('showImg/', showImg)
	re_path(r'^post/new/$', post_new, name='post_new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)