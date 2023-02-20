bilets = int(input("Количество билетов: "))
tax = 0

for t in range(bilets):
    age = int(input(f'Введите возраст {t+1} посетителя: '))

    if age >= 25:
        tax += 1390

    elif 18 <= age < 25:
        tax += 990

if bilets >= 3:
    tax = int(tax * 0.9)

print(f'К оплате: {str(tax)} руб.')
