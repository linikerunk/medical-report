import string
from django.test import TestCase
from model_mommy import mommy

from core.models import Examination, MedicalExam


class TestSaveExamination(TestCase):

    def setUp(self):
        name = string.ascii_lowercase 
        generate_name = ''.join(random.choice(name) for i in range(0, 10))
        self.doctor_name = generate_name

    def check_upper_name(self):
        medical_exam = MedicalExam.objects.all().first() 
        self.assertTrue(medical_exam.doctor_name.isupper())
