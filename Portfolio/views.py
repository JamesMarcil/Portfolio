from django.views.generic import TemplateView

from projects.models import Project

class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        xs = Project.objects.all().order_by('title', 'language')
        for x in xs:
            x.url = x.title.replace(' ', '_')
        context['projects'] = xs
        return context

class IndexView(BaseView):
    template_name = 'index.html'

class AboutView(BaseView):
    template_name = 'about.html'

class ContactView(BaseView):
    template_name = 'contact.html'
