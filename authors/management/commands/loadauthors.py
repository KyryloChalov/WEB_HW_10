from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from authors.models import Author
import json


class Command(BaseCommand):
    help = "Upload authors from json to db"

    def add_arguments(self, parser):
        parser.add_argument('path', nargs=1)

    def handle(self, *args, **options):
        path = options['path'][0]
        try:
            with open(path) as file:
                data = json.load(file)
                authors = []
                for author_data in data:
                    author_data["born_date"] = datetime.strptime(author_data['born_date'], "%B %d, %Y").date()
                    authors.append(Author(**author_data))
                Author.objects.bulk_create(authors)
        except FileNotFoundError:
            raise CommandError('File "%s" not found' % path)
