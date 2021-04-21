value = {"USD": ["доллар", "$", "dollar"], "RUB": ["руб", "rubl"], "EUR": ["евро", "euro"]}

# Функция принимает в себя часто используемые имена валют и заменяет на необходимые сокращения
def chek(val):
    for key in value:
        for j in value[key]:
            if j.upper() in val:
                return key
    return val
