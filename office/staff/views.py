from django.shortcuts import render, HttpResponse, get_object_or_404
from datetime import datetime
from .models import Department, Role, Employee
from django.views.decorators.csrf import requires_csrf_token
from django.db.models import Q

# Home Page
def index(request):
    employees = Employee.objects.all()
    context = {"emps": employees}
    return render(request, "index.html", context)

# Display All Employees
def all_emp(request):
    employees = Employee.objects.all()
    context = {"emps": employees}
    return render(request, "all_emp.html", context)

# Add New Employee
@requires_csrf_token
def add_emp(request):
    context = {
        "departments": Department.objects.all(),
        "roles": Role.objects.all(),
    }

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        salary = request.POST.get("salary")
        bonus = request.POST.get("bonus")
        phone = request.POST.get("phone")
        dept = request.POST.get("dept")
        role = request.POST.get("role")

        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            phone=phone,
            dept_id=dept,
            role_id=role,
            date_hire=datetime.now(),
        )
        new_emp.save()
        return HttpResponse("<h1>Employee created successfully!</h1>")

    return render(request, "add_emp.html", context)

# Delete Employee
def del_emp(request, emp_id=0):
    if emp_id:
        emp_delete = get_object_or_404(Employee, id=emp_id)
        emp_delete.delete()
        return HttpResponse("<h1>Employee deleted successfully!</h1>")

    employees = Employee.objects.all()
    context = {"emps": employees}
    return render(request, "del_emp.html", context)

# Filter Employees
def filter_emp(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        role = request.POST.get("role", "").strip()
        dept = request.POST.get("dept", "").strip()
        
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__dept_name__icontains=dept)
        if role:
            emps = emps.filter(role__role_name__icontains=role)

        context = {"emps": emps}
        return render(request, "filter_emp.html", context)

    return render(request, "filter_emp.html", {"emps": Employee.objects.all()})
