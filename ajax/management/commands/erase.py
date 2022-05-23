# Imports -------------------------------------------------------------------------------------------------------------

from django.core.management.base import BaseCommand, CommandError
from ajax.models import Category, Question, Answer


# Command class to be run with manage.py ------------------------------------------------------------------------------

class Command(BaseCommand):
    help = 'Erase the database'

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Question.objects.all().delete()
        Answer.objects.all().delete()

        self.stdout.write('Database has been erased!')
