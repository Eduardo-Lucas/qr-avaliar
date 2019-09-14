from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.db.models import Q
from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from polls.forms import ChoiceForm, QuestionForm, QuestionChoiceFormSet
from polls.models import Question, Choice


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class QuestionList(ListView):
    model = Question
    template_name = "polls/question-list.html"

    def get_queryset(self):
        valor = self.request.GET.get('q')
        if valor:
            object_list = self.model.objects.filter(
                Q(question_text__icontains=valor)
            )
        else:
            object_list = self.model.objects.all()

        paginator = Paginator(object_list, 10)  # Show 10 contas per page

        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)

        # return object_list
        return queryset


class QuestionDetail(DetailView):
    model = Question
    template_name = "polls/question-detail.html"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.question_text,
        )


class QuestionCreate(CreateView):
    form_class = QuestionForm
    template_name = 'polls/pergunta_form.html'

    def get_context_data(self, **kwargs):
        data = super(QuestionCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['choices'] = QuestionChoiceFormSet(self.request.POST)
        else:
            data['choices'] = QuestionChoiceFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        choices = context['choices']
        with transaction.atomic():
            # form.instance.created_by = self.request.user
            self.object = form.save()
        if choices.is_valid():
            choices.instance = self.object
            choices.save()

        return super(QuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('polls:question-list')
