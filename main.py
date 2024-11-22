import os


"""Указать в консоли нормализованный абсолютный путь к
файлу test_file_1.txt"""
path_test_file_1 = os.path.normpath(r"C:\Users\User\Desktop\home_work_deadline_25_11\data_path_1\test_file_1.txt")
print(f"абсолютный путь к файлу test_file_1.txt - {path_test_file_1}")
print()


"""При помощи функции os.walk() вывести в консоль
содержимое папки вашего нового проекта"""
for path, dirnames, filenames in os.walk(r"C:\Users\User\Desktop\home_work_deadline_25_11\data_path_1"):
    print(f"path - {path}")
    print(f"dirnames - {dirnames}")
    print(f"filenames - {filenames}")
print()


"""При помощи метода os.path.join() cоставить
нормализованный абсолютный путь к файлу
test_file_3.txt"""
abs_dir = r"C:\Users\User\Desktop\home_work_deadline_25_11\data_path_2"
test_file_3 = "test_file_3.txt"
dir_path = os.path.join(abs_dir, test_file_3)
normpath_dir = os.path.normpath(dir_path)
print(f"нормализованный абсолютный путь к файлу test_file_3.txt - {normpath_dir}")
print()


"""Написать код для создания и для удаления папки внутри
папки data_path_2"""
base_dir = "."
data_path_2_dir = r"data_path_2"
new_dir = r"new_dir"

add_new_dir = os.path.join(base_dir, data_path_2_dir, new_dir)

if os.path.exists(add_new_dir) is False:
    os.mkdir(add_new_dir)
    print(f"The directory '{new_dir}' created")
else:
    print("That directory already exists")
    print(add_new_dir)
print()

"""удаления папки внутри
папки data_path_2"""
if os.path.exists(add_new_dir) is True:
    os.rmdir(add_new_dir)
    print(f"That directory '{new_dir}' deleted")
else:
    print("That directory doesn't exist")
print()


"""Вам необходимо написать функцию которая запишет в
файл следующий текст. Записать должно именно так как
указано в задании (а именно не сплошной текст а несколько
строк в столбик).
1.
Вам необходимо написать функцию которая бы считала
текст из созданного вами в первом задании файла и вывела
результат в консоль. Вывести его нужно именно так как и
было записано, построчно без разрывов между строками. """

path_to_test_file_1 = os.path.normpath(r"data_path_1\test_file_1.txt")

def write_data(data):
    get_data = data.split(",")
    with open(path_to_test_file_1, "w", encoding="utf-8") as file:
        for text in get_data:
            file.write(f"{text}\n")
    print("Данные записаны")
    print()


my_text = "Если б мишки были пчелами,То они бы нипочем,Никогда и не подумали,Так высоко строить дом."
write_data(my_text)


def read_data():
    with open(path_to_test_file_1, "r", encoding="utf-8") as file:
        content = file.readlines()
        for text in content:
            print(text.rstrip())


read_data()