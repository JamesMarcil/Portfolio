from django.conf.urls   import url

from .views             import ProjectsView, ProjectView

urlpatterns = [
	url(r'^$', ProjectsView.as_view(), name='projects'),
	url(r'^(?P<project_name_url>\w+)/$', ProjectView.as_view(), name='project')
]
