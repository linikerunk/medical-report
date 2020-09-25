from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.core import serializers
import json

from .models import MedicalExam, Examination


class IndexView(ListView):

    model = MedicalExam
    paginate_by = 10
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['medical_exam'] = MedicalExam.objects.all()
        return context


def doctor_name_ajax(request, id):
    doctor_name = MedicalExam.objects.filter(guide_number=id)
    print("Serializado : ", serializers.serialize('json', doctor_name))
    return JsonResponse(serializers.serialize('json', doctor_name), safe=False)