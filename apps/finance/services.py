from .models import Record
from django.db.models import Sum

def get_summary():
    income = Record.objects.filter(type="income").aggregate(Sum("amount"))["amount__sum"] or 0
    expense = Record.objects.filter(type="expense").aggregate(Sum("amount"))["amount__sum"] or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }