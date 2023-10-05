import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','satyamjobs.settings')
import django
django.setup()


from testapp.models import *
from faker import Faker
from random import *
fake= Faker()

def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project Manager','Team Lead','Software Engineer','Associate Engineer'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','MBA'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hyd_jobs_records=HydJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)

    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(
                elements=('project Manager', 'Team Lead', 'Software Engineer', 'Associate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech', 'M.Tech', 'MCA', 'MBA'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        pune_jobs_records = PuneJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle,
                                                             eligibility=feligibility, address=faddress, email=femail,
                                                             phonenumber=fphonenumber)

    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(
                elements=('project Manager', 'Team Lead', 'Software Engineer', 'Associate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech', 'M.Tech', 'MCA', 'MBA'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        bang_jobs_records = BangJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle,
                                                             eligibility=feligibility, address=faddress, email=femail,
                                                             phonenumber=fphonenumber)

n=int(input('Enter number of records:'))
populate(n)
print(f'{n} records inserted successfully......')
