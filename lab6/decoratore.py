def checkcpu(func):
    def wrapper(*args, **kwargs):
        cpu = None
        if len(args) >= 3:
            a = args[0]
            b = args[1]
            cpu = args[2]
            
        if a is not None and b is not None:
            if a+b >= 100: cpu += 50
            elif a+b >= 50: cpu += 30
            elif a+b >= 25: cpu += 10
        if cpu >= 50:
            print(f'Не можу виконати це завдання — CPU перевищено: {cpu}%)')
            return None
            print("cpu:", cpu)

        return func(*args, **kwargs)

    return wrapper

