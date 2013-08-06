from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.VisualStyleView.as_view(), name="style_details"),
    url(r'^(?P<active_template_filename>.+)$',
        views.VisualStyleView.as_view(), name="style_details"),
)
