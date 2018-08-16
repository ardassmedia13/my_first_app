from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic.base import TemplateView


urlpatterns = [
    url('', TemplateView.as_view(template_name='index.html'), name='index'),
    url('mysite/', include('mysite.urls')),
    url('admin/', admin.site.urls),

]
