from django.core.management.base import BaseCommand
from post.models import Post  

class Command(BaseCommand):
    help = 'Creates 100 Post objects'

    def handle(self, *args, **options):
        for i in range(1, 101):
            Post.objects.create(
                title=f"Post {i}",
                content=f"Content of Post {i}"
            )
            self.stdout.write(self.style.SUCCESS('Successfully created Post objects'))
            
        self.stdout.write(self.style.SUCCESS('Successfully created 100 Post objects'))
