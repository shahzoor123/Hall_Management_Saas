from django.db import models

class Salary(models.Model):

    guards = 'Guards'
    marquee_staff = 'Marquee Staff'
    office_staff = 'Office Staff'

    EMPLOYEE_TYPE = ((guards, 'Guards'),
                  (marquee_staff, 'Marquee Staff'),
                  (office_staff, 'Office Staff'),
                  )

    employee_type = models.CharField(choices=EMPLOYEE_TYPE, max_length=20)
    details = models.CharField(max_length=300, blank=True)
    amount = models.IntegerField(default=0)
    on_date = models.DateField()
    expense_by = models.CharField(max_length=50)



class DailyExpenses(models.Model):

    cards = 'Cards'
    internet = 'Internet Bill'
    tea = 'Tea'
    utility_bills = 'Utility Bills'
    food = "Food"
    others = "Other Expenses"

    EXPENSE_TYPE = ((cards, 'Cards'),
                  (internet, 'Internet Bill'),
                  (tea, 'Tea'),
                  (utility_bills, 'Utility Bills'),
                  (food, 'Food'),
                  (others, 'Others Expenses'),
                  )

    expense_type = models.CharField(choices=EXPENSE_TYPE, max_length=20)
    details = models.CharField(max_length=300, blank=True)
    amount = models.IntegerField(default=0)
    on_date = models.DateField()
    expense_by = models.CharField(max_length=50)


class ConstructionAndRepair(models.Model):
    
    expense_for = models.CharField(max_length=200)
    details = models.CharField(max_length=300, blank=True)
    amount = models.IntegerField(default=0)
    on_date = models.DateField()
    expense_by = models.CharField(max_length=50)

class OtherExpense(models.Model):
    
    rent = 'Rents'
    tax = 'Taxes'
    online_expense = 'Online Expense'
    other = "Other Expense"
    EXPENSE_TYPE = ((rent, 'Rents'),
                  (tax, 'Taxes'),
                  (online_expense, 'Online Expense'),
                  (other, 'Other Expense'),
                  )

    expense_type = models.CharField(choices=EXPENSE_TYPE, max_length=20)
    details = models.CharField(max_length=300, blank=True)
    amount = models.IntegerField(default=0)
    on_date = models.DateField()
    expense_by = models.CharField(max_length=50)

