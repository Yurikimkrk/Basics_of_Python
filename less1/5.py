# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма (прибыль - выручка больше издержек или убыток
# - издержки больше выручки). Выведите соответствующее сообщение. Если фирма
# отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к
# к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

revenue = input("Enter the firm's revenue($): ")
costs = input("Enter the firm's costs($): ")
while not revenue.isdigit() or not costs.isdigit():
    print("Please, reEnter")
    revenue = input("Enter the firm's revenue($): ")
    costs = input("Enter the firm's costs($): ")
revenue = int(revenue)
costs = int(costs)
if costs > revenue:
    print("The firm worked at a loss")
elif costs == revenue:
    print("The firm worked in zero")
else:
    print("The firm worked in plus")
    profitability = ((revenue - costs) / revenue) * 100
    staff = input("Enter the number of firm's staff: ")
    while not staff.isdigit() or staff == "0":
        staff = input("Enter the number of firm's staff (>0): ")
    staff = int(staff)
    profit_per_staff = (revenue - costs) / staff
    print(f"Firm's profitabiblity = {profitability:.1f}%, profit per 1 staff = {profit_per_staff:.1f}$")
