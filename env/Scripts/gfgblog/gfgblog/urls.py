from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
	# urls handling admin route
	path('admin/', admin.site.urls),
	# urls handling blog routes
	path('', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

