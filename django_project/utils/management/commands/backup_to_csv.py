
import os
import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from django.apps import apps
from datetime import datetime

class Command(BaseCommand):

    def handle(self, *args, **options):
        model_list = apps.get_models()
        model_name_list = [x.__name__ for x in model_list]

        for model in model_list:
            all_fields = model._meta.get_fields()
            columns = [x.name for x in all_fields]
             
            time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            path_dir = os.path.join(settings.ROOT_DIR, 'backup_DB', f'csvs-{time}')
            if not os.path.exists(path_dir):
                os.makedirs(str(path_dir))

            path = os.path.join(path_dir,f"{model.__name__}.csv")
            with open(path, mode='w') as csv_file:
                writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                # Writing column names
                writer.writerow(columns)

                objects = model.objects.all()

                for obj in objects:
                    row = [str(getattr(obj, field_name,"NA")) for field_name in columns]
                    writer.writerow(row)

        self.stdout.write(self.style.SUCCESS(f'backup models to csv successfully'))

