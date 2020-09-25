from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import MedicalExam, Examination


@admin.register(MedicalExam)
class MedicalExamAdmin(ImportExportModelAdmin):
    list_display = ['guide_number', 'doctor_identifier', 'doctor_name',
    'query_date', 'query_value' ]
    list_filter = ['doctor_name', 'query_date']


@admin.register(Examination)
class ExaminationAdmin(ImportExportModelAdmin):
    list_display = ['guide_number', 'exam_name', 'exam_times']
    list_filter = ['guide_number', 'exam_name']