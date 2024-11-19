# load_data.py
import os
import django
import json
from django.apps import apps
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pathways.settings')
django.setup()


def parse_datetime(datetime_str):
    if datetime_str:
        dt = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        return make_aware(dt)
    return None


def load_data(json_file):
    try:
        with open(json_file) as f:
            data = json.load(f)

        if not isinstance(data, list):
            data = [data]

        for item in data:
            try:
                # Get model
                app_label, model_name = item['model'].split('.')
                model_class = apps.get_model(app_label, model_name)

                # Prepare fields
                fields = item['fields']

                # Convert datetime strings to datetime objects
                if 'created_at' in fields:
                    fields['created_at'] = parse_datetime(fields['created_at'])
                if 'updated_at' in fields:
                    fields['updated_at'] = parse_datetime(fields['updated_at'])

                # Set id if pk exists
                if 'pk' in item:
                    fields['id'] = item['pk']

                # Create object
                obj = model_class.objects.create(**fields)
                print(f'Successfully created {model_name} object: {obj.name} (ID: {obj.id})')

            except Exception as e:
                print(f'Failed to create object from: {item["model"]}\nError: {str(e)}')

    except FileNotFoundError:
        print(f'File {json_file} not found')
    except json.JSONDecodeError:
        print('Invalid JSON file')
    except Exception as e:
        print(f'Error: {str(e)}')


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python load_data.py <json_file>')
    else:
        load_data(sys.argv[1])
