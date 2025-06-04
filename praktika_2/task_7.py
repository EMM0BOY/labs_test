def count_patients(filename, city, max_age):
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 5:
                surname, gender, age, patient_city, diagnosis = (
                    parts[0],
                    parts[1],
                    int(parts[2]),
                    parts[3],
                    " ".join(parts[4:]),
                )
                if patient_city == city and age < max_age:
                    count += 1
    return count


filename = "klinika.txt"
city = input("Введите название города (X): ")
max_age = int(input("Введите максимальный возраст (Y): "))
result = count_patients(filename, city, max_age)
print(f"Количество пациентов младше {max_age} лет из города {city}: {result}")
