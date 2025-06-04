from datetime import datetime, date

now = datetime.now()
current_date = now.date()
current_time = now.time()
weekday_number = now.weekday()
target_date = date(2025, 6, 1)
days_remaining = (target_date - current_date).days
print(f"Сегодняшняя дата: {current_date}")
print(f"Текущее время: {current_time.strftime('%H:%M:%S')}")
print(f"Номер дня недели (0 - понедельник): {weekday_number}")
print(f"Дней до 1 июня 2025 года: {days_remaining}")
