from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# # Create your views here.
# def index(request):
#     latest_question_list = Question.objects.all()
#     return render(request,"polis/index.html",{
#         "latest_question_list": latest_question_list
#     })


# def detail(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,"polis/detail.html",{
#         "question": question
#     })


# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, "polis/results.html",{
#         "question": question
#     })


class IndexView(generic.ListView):
    template_name = "polis/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polis/detail.html"
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polis/results.html"    


def vote(request,question_id):
    question = get_object_or_404(Question ,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError,Choice.DoesNotExist):
        return render(request,"polis/detail.html",{
            "question": question,
            "error_message": "No eligiste una respuesta"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polis:results",args=(question.id,)))
