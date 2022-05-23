from django.core.management.base import BaseCommand, CommandError

import ruamel.yaml as yaml
import json

from ajax.models import Category, Question, Answer


class Command(BaseCommand):
    help = 'Read a a YAML file to populate the database'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='Name of YAML file to be used')

    def handle(self, *args, **kwargs):
        file = kwargs['file_name']

        with open(file) as stream:
            try:
                yaml_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                yaml_data = None


        print(json.dumps(yaml_data, indent=2))

        for category in yaml_data:
            print("category: " + category)
            cat, created = Category.objects.get_or_create(category=category)
            for question in yaml_data[category]:
                value = yaml_data[category][question]['value']
                print("  question: " + question)
                print("     value: " + str(value))
                quest, created = Question.objects.get_or_create(question=question, category=cat, value=value)
                for answer in yaml_data[category][question]['answers']:
                    if (type(answer) is dict):
                        correct_answer_string = str(next(iter(answer)))
                        correct_answer, created = Answer.objects.get_or_create(answer=correct_answer_string, question=quest)
                        print("    answer: " + correct_answer.answer + " CORRECT")
                        quest.correct_answer = correct_answer
                        quest.save()
                    else:
                        print("    answer: " + str(answer))
                        ans, created = Answer.objects.get_or_create(answer=answer, question=quest)

        print('Database has been initialized with the {} file'.format(file))
