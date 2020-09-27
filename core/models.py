import datetime
from django.db import models


class Base(models.Model):
    created = models.DateField('Criação',auto_now_add=True)
    modified = models.DateField('Atualização',auto_now=True)
    active = models.BooleanField('Ativo',default=True)

    class Meta:
        abstract = True


class MedicalExam(Base):
    guide_number = models.AutoField(primary_key=True,editable=False)
    doctor_identifier = models.PositiveIntegerField('Código do Médico')
    doctor_name = models.CharField('Nome do Médico',max_length=100)
    query_date =  models.DateField("Date", default=datetime.date.today)
    query_value = models.DecimalField(
        "Valor da Consulta",
        max_digits=8,
        decimal_places=2,
    )

    class Meta:
        verbose_name = 'Consulta Médica'
        verbose_name_plural = 'Consultas Médicas'

    def save(self, *args, **kwargs):
        self.doctor_name = self.doctor_name.upper()
        return super(MedicalExam, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.guide_number}"


class Examination(Base):
    guide_number = models.ForeignKey(
        'core.MedicalExam',
        verbose_name="Número da Guia",
        on_delete=models.PROTECT
    )
    exam_name = models.CharField("Nome do Exame", max_length=100)
    exam_times = models.PositiveIntegerField("Número de Exames", null=True)

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

    def save(self, *args, **kwargs):
        self.exam_name = self.exam_name.upper()
        return super(Examination, self).save(*args, **kwargs)

    def get_total_value_exam(self):
        return self.guide_number.query_value * self.exam_times

    def __str__(self):
        return self.exam_name