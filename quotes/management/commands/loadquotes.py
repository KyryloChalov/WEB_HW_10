from django.core.management.base import BaseCommand, CommandError
from quotes.models import Tag, Quote
from authors.models import Author
import json


class Command(BaseCommand):
    help = "Upload quotes from json to db"

    def add_arguments(self, parser):
        parser.add_argument('path', nargs=1)

    def handle(self, *args, **options):
        path = options['path'][0]
        try:
            with open(path) as file:
                data = json.load(file)
                tags = set()
                quotes = []
                for quote_data in data:
                    [tags.add(tag) for tag in quote_data['tags']]
                    author = Author.objects.filter(fullname=quote_data['author']).first()
                    quotes.append({
                        "quote": Quote(quote=quote_data['quote'], author=author),
                        "tags": quote_data["tags"]
                    })
                tags = [Tag(name=tag) for tag in tags]
                Tag.objects.bulk_create(tags)

                for quote_data in quotes:
                    tags_lst = Tag.objects.filter(name__in=quote_data["tags"]).all()
                    quote_data["quote"].save()
                    quote_data["quote"].tags.set(tags_lst)
        except FileNotFoundError:
            raise CommandError('File "%s" not found' % path)
