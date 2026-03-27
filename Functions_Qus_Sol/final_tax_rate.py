def check_final_tax_rate(salary):
    if salary < 3000:
        return "5%"
    elif 3000 < salary < 7000:
        return "15%"
    elif salary > 7000:
        return "25%"

print("your tax will be", check_final_tax_rate(1000))