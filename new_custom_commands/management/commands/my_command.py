from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'some info about the cmd'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Specify username')

        parser.add_argument('--upper', action="store_true", help='To UpperCase', required=False)

    def handle(self, *args, **options):
        self.check()

        # self.stdout.writelines(["h", 'd'])

        # self.stdout.write("stdout")

        # self.stderr.write("stderr")

        # self.stdout.write(self.style.SUCCESS("SUCCESS"))
        # self.stdout.write(self.style.ERROR("ERROR"))
        # self.stdout.write(self.style.WARNING("WARNING"))

        username = options.get('username')

        if options.get('upper'):
            self.stdout.write(self.style.SUCCESS(f"Hell {username.upper()}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Hell {username}"))
        

    