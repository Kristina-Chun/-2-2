
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
no_debts=money_capital+salary-spend
month=0
while no_debts>0:
    spend=spend+spend*increase
    no_debts=no_debts+salary-spend
    month +=1
print("Количество месяцев, которое можно протянуть без долгов:", month)
