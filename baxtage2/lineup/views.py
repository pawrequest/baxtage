from django.views.generic import CreateView, DetailView, ListView

from lineup.forms import PerformanceForm
from lineup.models import Performance


class PerformanceCreateView(CreateView):
    model = Performance
    form_class = PerformanceForm
    template_name = 'lineup/performance_form.html'
    success_url = '/lineup/'


class PerformanceListView(ListView):
    model = Performance
    context_object_name = 'performances'
    template_name = 'lineup/performance_list.html'  # Update this with the correct template name


class PerformanceDetailView(DetailView):
    model = Performance
    context_object_name = 'performance'
    template_name = 'lineup/performance_detail.html'  # Update this with the correct template name
