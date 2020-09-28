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
        doctor_name = self.request.GET.get('doctor_identifier') 

        try:
            term = term.replace('/', '-')
            term_formated = datetime.strptime(term, '%d-%m-%Y').strftime(
                                                    '%Y-%m-%d')
            qs = super().get_queryset(*args, **kwargs)

            if not term_formated:
                return qs

            if term_formated:
                qs = qs.filter(
                    guide_number__query_date=term_formated).order_by(
                            '-guide_number__total_value')
            
            if doctor_name:
                qs = qs.filter()
                
        except Exception as e:
            print(f'Campo de pesquisa está vazio, erro : {e}')
            qs = super().get_queryset(*args, **kwargs)
        return qs
