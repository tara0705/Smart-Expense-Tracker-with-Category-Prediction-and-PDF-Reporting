from django.shortcuts import render, redirect
from .models import Expense, Salary
from django.db.models import Sum
from .utils import predict_category
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Expense

def dashboard(request):

    expenses = Expense.objects.all()

    total_expense = Expense.objects.aggregate(Sum("amount"))["amount__sum"] or 0

    salary = Salary.objects.first()

    salary_amount = salary.amount if salary else 0
    balance = salary_amount - total_expense

    context = {
        "expenses": expenses,
        "salary": salary_amount,
        "total_expense": total_expense,
        "balance": balance
    }

    return render(request, "tracker/dashboard.html", context)


def add_expense(request):

    if request.method == "POST":

        title = request.POST.get("title")
        amount = request.POST.get("amount")

        category = predict_category(title)

        Expense.objects.create(
            title=title,
            amount=amount,
            category=category
        )

        return redirect("/")

    return render(request, "tracker/add_expense.html")


def set_salary(request):

    if request.method == "POST":

        amount = request.POST.get("salary")

        Salary.objects.all().delete()

        Salary.objects.create(amount=amount)

        return redirect("/")

    return render(request, "tracker/set_salary.html")

def export_pdf(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="expenses.pdf"'

    p = canvas.Canvas(response)

    expenses = Expense.objects.all()

    y = 800

    p.setFont("Helvetica", 14)
    p.drawString(200, 820, "Expense Report")

    p.setFont("Helvetica", 12)

    for expense in expenses:
        text = f"{expense.title} | {expense.category} | ₹{expense.amount}"
        p.drawString(50, y, text)
        y -= 30

    p.showPage()
    p.save()

    return response