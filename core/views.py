import json
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
    '''
    https://docs.djangoproject.com/en/3.0/topics/db/queries/#complex-lookups-with-q-objects
    '''

    def get_queryset(self, *args, **kwargs):

        term = self.request.GET.get('term', None)
        doctor_identifier = self.request.GET.get('doctor_identifier', None)

        try:
            
            qs = super().get_queryset(*args, **kwargs)

            filtros = None

            if term:
                term = term.replace('/', '-')
                term_formated = datetime.strptime(term, '%d-%m-%Y').strftime(
                                                    '%Y-%m-%d')

                filtros = Q(guide_number__query_date=term_formated)
                
                                                    
            if doctor_identifier:
                filtros = Q(guide_number__doctor_identifier=doctor_identifier)
            
            if term and doctor_identifier:
                filtros = Q(guide_number__query_date=term_formated) & Q(
                    guide_number__doctor_identifier=doctor_identifier)

            qs = qs.filter(filtros)

        except Exception as e:
            print(f'Campo de pesquisa está vazio, erro : {e}')
            qs = super().get_queryset(*args, **kwargs)

        return qs
