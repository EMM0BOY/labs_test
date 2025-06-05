import os
import time

# Получаем список файлов в текущей директории
files = [f for f in os.listdir() if os.path.isfile(f)]

if not files:
    print("В директории нет файлов")
else:
    target_file = files[0]
    file_stats = os.stat(target_file)
    creation_time = time.ctime(file_stats.st_ctime)
    modification_time = time.ctime(file_stats.st_mtime)

    with open("inf.txt", "w", encoding="utf-8") as f:
        f.write(f"Информация о файле: {target_file}\n")
        f.write("=" * 40 + "\n")
        f.write(f"Размер файла: {file_stats.st_size} байт\n")
        f.write(f"Дата создания: {creation_time}\n")
        f.write(f"Дата последнего изменения: {modification_time}\n")
        f.write(f"Режим доступа: {oct(file_stats.st_mode)[-4:]}\n")
        f.write(f"Владелец (UID): {file_stats.st_uid}\n")
        f.write(f"Группа (GID): {file_stats.st_gid}\n")

    print(f"Информация о файле '{target_file}' записана в inf.txt")
