from django.db.models import F
from core.models import Employee

# Grant a 10% salary increase directly inside the DB engine (Atomic)
Employee.objects.filter(department__code="IT").update(salary=F('salary') * 1.10)

for emp in Employee.objects.filter(department__code="IT"):
    print(f"{emp.first_name} New Salary: {emp.salary}")