import csv
import re
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            regex = re.compile('(\d{4})-(\d{2})-(\d{2})')

            for phone in phones:
                name = phone['name']
                image = phone['image']
                price = float(phone['price'])
                date = regex.findall(phone['release_date'])
                release_date = datetime(int(date[0][0]), int(date[0][1]), int(date[0][2]))
                slug = slugify(name)
                lte_exists = bool(phone['lte_exists'])
                Phone.objects.create(name=name, image=image, price=price, release_date=release_date,
                                     lte_exists=lte_exists, slug=slug)

    def get_phones(self):
        return Phone.objects.filter()