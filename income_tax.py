user_name = input("введите ваше имя: ")
user_money = float(input("ваш доход: "))
money_and_tax = (user_money*(1+0.135))
print(f"""мистер {user_name} 
      ваш доход с учетом налогов составляет - {money_and_tax} рублей.""")