import json
from datetime import datetime
from django.core.paginator import Paginator
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView

from .models import MedicalExam, Examination


class IndexView(ListView):

    model = MedicalExam
    paginate_by = 10
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
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
            qs = MedicalExam.objects.filter(query_date=term_formated)
        except:
            qs = super().get_queryset(*args, **kwargs)
        return qs
            



def doctor_name_ajax(request, id):
    doctor_name = MedicalExam.objects.filter(guide_number=id)
    print("Serializado : ", serializers.serialize('json', doctor_name))
    return JsonResponse(serializers.serialize('json', doctor_name), safe=False)