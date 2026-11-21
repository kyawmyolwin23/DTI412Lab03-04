from core.models import Department, Employee, Course, TrainingRecord

# Create Departments
hr = Department.objects.create(name="Human Resources", code="HR")
it = Department.objects.create(name="Information Technology", code="IT")
fin = Department.objects.create(name="Finance", code="FIN")

# Create Employees
e1 = Employee.objects.create(
    employee_code="EMP001",
    first_name="John",
    last_name="Doe",
    email="john@example.com",
    salary=65000.00,
    department=it
)
e2 = Employee.objects.create(
    employee_code="EMP002",
    first_name="Jane",
    last_name="Smith",
    email="jane@example.com",
    salary=75000.00,
    department=it
)
e3 = Employee.objects.create(
    employee_code="EMP003",
    first_name="Alice",
    last_name="Johnson",
    email="alice@example.com",
    salary=55000.00,
    department=hr
)
e4 = Employee.objects.create(
    employee_code="EMP004",
    first_name="Bob",
    last_name="Brown",
    email="bob@example.com",
    salary=60000.00,
    department=fin
)

# Create Courses
c1 = Course.objects.create(code="SEC101", title="Cybersecurity Essentials", capacity=25)
c2 = Course.objects.create(code="DEV201", title="Advanced Django ORM", capacity=30)

# Create Training Records
TrainingRecord.objects.create(
    employee=e1,
    course=c1,
    completion_status="COMPLETED",
    score=88.50
)
TrainingRecord.objects.create(
    employee=e1,
    course=c2,
    completion_status="IN_PROGRESS"
)
TrainingRecord.objects.create(
    employee=e2,
    course=c2,
    completion_status="COMPLETED",
    score=95.00
)
TrainingRecord.objects.create(
    employee=e3,
    course=c1,
    completion_status="REGISTERED"
)

exit()