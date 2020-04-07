from.models import user,Task,Advices
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Command(BaseCommand):
    def import_data_from_file(self):
        data_folder = os.path.join(BASE_DIR,'import','resource/json_file')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder,data_file),encoding ='utf - 8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    title = data_object.get('title',None)
                    url = data.object.get('url',None)

    def handler(self, *args,**options):
        self.import_data_from_file()
