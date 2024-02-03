from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.db.models import Count
from django.shortcuts import redirect
from .models import Quote, Tag


# Create your views here.
class MainPageView(ListView):
    template_name = 'quotes/index.html'
    context_object_name = 'quotes_list'
    model = Quote
    paginate_by = 10
    top_tags_count = 10

    def get_context_data(self, *args, **kwargs):
        context = super(MainPageView, self).get_context_data(*args, **kwargs)
        context['top_tags'] = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
        return context


class TagPageView(DetailView):
    template_name = 'quotes/tag.html'
    model = Tag
    context_object_name = 'tag'


class CreateQuoteView(CreateView):
    model = Quote
    fields = ['quote', 'tags', 'author']
    template_name = 'quotes/quote_create_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(to='quotes:create.quote')
