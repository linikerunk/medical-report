# Generated by Django 2.2.7 on 2020-09-25 02:48
import csv
from django.db import migrations
from core.models import MedicalExam, Examination


def insert_query_models(apps, schema_editor):
    with open("data_migrations/consulta.csv", "r+") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for row  in csv_reader:
            print(row)
            try:
                obj = MedicalExam.objects.create(
                    guide_number=row[0],
                    doctor_identifier=row[1],
                    doctor_name=row[2],
                    query_date=row[3],
                    query_value=row[4],)
                obj.save()
            except MedicalExam.DoesNotExist:
                print("Objeto não existe.")

def insert_exam_models(apps, schema_editor):
    with open("data_migrations/exames.csv", "r+") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for row  in csv_reader:
            print(row)
            try:
                obj_guide_number = MedicalExam.objects.get(
                    guide_number = row[0])
                obj = Examination.objects.create(
                    guide_number=obj_guide_number,
                    exam_name=row[1],
                    exam_times=row[2],)
                obj.save()
            except Examination.DoesNotExist:
                print("Objeto não existe.")




class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_query_models),
        migrations.RunPython(insert_exam_models),
    ]