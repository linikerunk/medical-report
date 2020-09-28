import json, simplejson
from datetime import datetime
from django.core.paginator import Paginator
from django.core import serializers
from django.db.models import Q, F
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView

from .models import MedicalExam, Examination


class IndexView(ListView):

    model = Examination
    paginate_by = 10
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['examination'] = Examination.objects.all()
        context['medical_exam'] = MedicalExam.objects.all()
        return context


class SearchView(IndexView):

    def get_queryset(self, *args, **kwargs):
        term = self.request.GET.get('term')
        try:
            term = term.replace('/', '-')
            term_formated = datetime.strptime(term, '%d-%m-%Y').strftime(
                                                    '%Y-%m-%d')
            qs = super().get_queryset(*args, **kwargs)

            if not term_formated:
                return qs
            qs = Examination.objects.filter(
                            guide_number__query_date=term_formated).order_by(
                                                '-guide_number__total_value')
        except Exception as e:
            print(f'Campo de pesquisa de data está vazio, erro : {e}')
            qs = super().get_queryset(*args, **kwargs)
        return qs
            





# View used by trying to do a request ajax but unfortunately
#  the query doens't work

# def doctor_name_ajax(request, id):
#     examination = Examination.objects.filter(
#                                   guide_number__doctor_identifier=id)
#     medical_exam = MedicalExam.objects.filter(doctor_identifier=id)
#     medical_exam = serializers.serialize('json', medical_exam)
#     examination = serializers.serialize('json', examination)
#     return JsonResponse(examination, safe=False)