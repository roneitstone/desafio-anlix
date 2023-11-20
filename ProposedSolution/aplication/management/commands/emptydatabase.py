from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from aplication.models import Paciente, Dado_Car, Dado_Pulm
import json
import os


 

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass
    def handle(self, *args, **options):
        Paciente.objects.all().delete()
        Dado_Car.objects.all().delete()
        Dado_Pulm.objects.all().delete()