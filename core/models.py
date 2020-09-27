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
    total_value = models.DecimalField(
        "Total da Consulta",
        max_digits=8,
        decimal_places=2,
        null=True,
    )

    class Meta:
        verbose_name = 'Consulta Médica'
        verbose_name_plural = 'Consultas Médicas'
        ordering = ['-total_value']
        

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
        ordering = ['-guide_number__total_value']

    def save(self, *args, **kwargs):
        self.exam_name = self.exam_name.upper()
        self.guide_number.total_value = self.guide_number.query_value * int(
                                                    self.exam_times)
        self.guide_number.save()
        return super(Examination, self).save(*args, **kwargs)

    # @property
    # def get_total_value_exam(self):
    #     return self.guide_number.query_value * int(self.exam_times)

    def __str__(self):
        return self.exam_name