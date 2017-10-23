import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

## FAKE POPULATION SCRIPT STARTED ##
import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Networking', 'Social', 'Gaming', 'News']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get topic for entry
        topic = add_topic()

        #Create fake data for entry
        fake_name = fakegen.company()
        fake_url = fakegen.url()
        fake_date = fakegen.date()

        #create webpage using fake entries
        wbpg = Webpage.objects.get_or_create(topic=topic, url=fake_url, name=fake_name)[0]

        #create access record using fake entry
        access_record = AccessRecord.objects.get_or_create(name=wbpg, date=fake_date)[0]


if __name__ == '__main__':
    print('populate started')
    populate(20)
    print('populate complete')
