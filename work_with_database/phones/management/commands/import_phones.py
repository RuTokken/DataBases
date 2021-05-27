import csv
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)

            for line in phone_reader:
                Phone.objects.create(name=line[1], image=line[2], price=line[3],
                                     slug=slugify(line[1], allow_unicode=True),
                                     release_date=line[4], lte_exists=line[5])