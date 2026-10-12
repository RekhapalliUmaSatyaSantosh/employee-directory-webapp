from django.shortcuts import render
import requests
from django.http import Http404

API_URL=' https://aamras.com/dummy/EmployeeDetails.json'
# Create your views here.
def get_employees():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    employees = data.get("employees", [])
    if not isinstance(employees, list):
        raise ValueError("Invalid employee data")
    return employees
    
def index(request):
    try:
        employees = get_employees()
        return render(request,"index.html",{"employees": employees})
    except (requests.RequestException, ValueError):
        return render(request,"index.html",{"employees": [],"error": "Unable to load employees. Please try again."})


def employee_details(request, employee_id):
    try:
        employees = get_employees()
    except (requests.RequestException, ValueError):
        raise Http404("Employee data is unavailable")
    if employee_id < 0 or employee_id >= len(employees):
        raise Http404("Employee not found")
    return render(request,"details.html",{"employee": employees[employee_id]})