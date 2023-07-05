from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.views.decorators.http import require_POST

from .models import Question, Choice, Case


class CaseListView(generic.ListView):
    model = Case
    template_name = 'case_list.html'
    context_object_name = 'cases'

    def get_queryset(self):
        # Dummy data creation
        Case.objects.create(title='Case 1',
                            description='Description of Case 1')
        Case.objects.create(title='Case 2',
                            description='Description of Case 2')
        Case.objects.create(title='Case 3',
                            description='Description of Case 3')

        return Case.objects.all()


@require_POST
def delete_case(request, id):
    case = Case.objects.get(id=id)
    case.delete()
    return redirect('cases:case_list')  # name of your case list URL


class IndexView(generic.ListView):
    template_name = "cases_service/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]


class DetailView(generic.DetailView):
    model = Question
    template_name = "cases_service/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "cases_service/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "ncsc_cases/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
