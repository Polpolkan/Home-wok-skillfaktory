cash = int(input("Введите сумму которую хотите положить на год:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
deposit_bank = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

accumulation_TKB = cash / 100 * per_cent['ТКБ']
accumulation_SKB = cash / 100 * per_cent['СКБ']
accumulation_VTB = cash / 100 * per_cent['ВТБ']
accumulation_SBER = cash / 100 * per_cent['СБЕР']

deposit.append(int(accumulation_TKB))
deposit.append(int(accumulation_SKB))
deposit.append(int(accumulation_VTB))
deposit.append(int(accumulation_SBER))

deposit_bank['ТКБ'] = accumulation_TKB
deposit_bank['СКБ'] = accumulation_SKB
deposit_bank['ВТБ'] = accumulation_VTB
deposit_bank['СБЕР'] = accumulation_SBER

max_bank_deposit = max(deposit_bank, key=deposit_bank.get)

print(deposit)
print('Максимальная сумма, которую вы можете заработать —', str(max(deposit)),"/", 'В банке -', str(max_bank_deposit),)
