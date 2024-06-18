from django.core.management.base import BaseCommand
from github_api.utils import fetch_github_repositories, save_github_repositories_to_db

class Command(BaseCommand):
    help = 'Fetch GitHub repositories and store in database'

    def handle(self, *args, **kwargs):
        try:
            repositories = fetch_github_repositories()
            save_github_repositories_to_db(repositories)
            self.stdout.write(self.style.SUCCESS('Successfully fetched and saved GitHub repositories'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
