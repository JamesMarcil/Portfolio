from django.views.generic   import TemplateView

from Portfolio.views        import BaseView
from .models                import Project

class ProjectsView(BaseView):
    template_name = 'projects/projects.html'

class ProjectView(BaseView):
    template_name = 'projects/project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        xs = Project.objects.all()
        for x in xs:
            x.url = x.title.replace(' ', '_')
        context['projects'] = xs

        project_name = self.kwargs['project_name_url']
        project_name = project_name.replace('_', ' ')
        project  = Project.objects.get(title = project_name)
        context['project'] = project

        return context
