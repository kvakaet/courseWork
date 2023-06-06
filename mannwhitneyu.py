import tkinter as tk
from tkinter import filedialog
import csv
from scipy.stats import mannwhitneyu

def program_data():
    welcome_window = tk.Toplevel(window)
    welcome_window.title("Данные о программе")
    label_welcome = tk.Label(welcome_window, text="Программа составлена студентом ПИЖ-б-о-21-1 Пуценко Иваном Алексеевичем")
    label_welcome.pack()

def instruction():
    large_text = """Добро пожаловать в приложение реализующее расчет U-критерия Манна-Уитни!
В меню "Файл" вы можете выбрать следующие опции:

"Данные о программе": Откроет новое окно с информацией о программе и ее авторе.
"Инструкция": Откроет новое окно с приветственным сообщением.
"Открыть CSV": Позволяет выбрать CSV-файл с данными для анализа.
После выбора опции "Открыть CSV" появится диалоговое окно, в котором вы можете выбрать CSV-файл с данными. 
Выберите нужный файл и нажмите "Открыть".

После открытия файла, данные из первых двух строк будут загружены и отображены в текстовых полях "Данные 1 выборки" и "Данные 2 выборки".

Введите необходимые значения в текстовые поля или оставьте значения по умолчанию.

Нажмите кнопку "Рассчитать", чтобы выполнить критерий Манна-Уитни для введенных данных.

Результаты анализа будут отображены под кнопкой в виде статистики и p-значения. 
Если p-значение больше 0.05, будет выведено сообщение, указывающее на отсутствие статистически значимой разницы между выборками. 
Если p-значение меньше или равно 0.05, будет выведено сообщение о наличии статистически значимой разницы между выборками.

Для выхода из программы выберите опцию "Выход" в меню "Файл" или закройте окно программы."""
    welcome_window = tk.Toplevel(window)
    welcome_window.title("Инструкция")
    label_welcome = tk.Label(welcome_window, text=large_text)
    label_welcome.pack()

def open_csv_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            separator = ": "
            data1 = "".join(next(reader)[0].split(separator)[1:]).split(' ')
            data2 = "".join(next(reader)[0].split(separator)[1:]).split(' ')

            entry_data1.delete(0, tk.END)
            entry_data1.insert(0, ", ".join(data1))
            entry_data2.delete(0, tk.END)
            entry_data2.insert(0, ", ".join(data2))

def calculate_mann_whitney():
    # Получение данных из текстовых полей
    data1 = [float(x.strip()) for x in entry_data1.get().split(",")]
    data2 = [float(x.strip()) for x in entry_data2.get().split(",")]

    # Расчет критерия Манна-Уитни
    statistic, p_value = mannwhitneyu(data1, data2)

    # Обновление метки с результатами
    if p_value > 0.05:
        label_result.config(
            text="Статистика: {:.2f}, p-значение: {:.2f}\nМежду данными выборками нет статистически значимой разницы.".format(
                statistic, p_value))
    else:
        label_result.config(
            text="Статистика: {:.2f}, p-значение: {:.2f}\nМежду данными выборками есть статистически значимая разница.".format(
                statistic, p_value))

# Создание графического интерфейса приложения
window = tk.Tk()
window.title("Критерий Манна-Уитни")

# Создание меню
menu = tk.Menu(window)
window.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Данные о программе", command=program_data)
file_menu.add_command(label="Инструкция", command=instruction)
file_menu.add_command(label="Открыть CSV", command=open_csv_file)
file_menu.add_command(label="Выход", command=window.quit)

# Создание меток и текстовых полей для ввода данных
label_data1 = tk.Label(window, text="Данные 1 выборки:")
label_data1.pack()
entry_data1 = tk.Entry(window)
entry_data1.pack()

label_data2 = tk.Label(window, text="Данные 2 выборки:")
label_data2.pack()
entry_data2 = tk.Entry(window)
entry_data2.pack()

# Кнопка для запуска расчета
button_calculate = tk.Button(window, text="Рассчитать", command=calculate_mann_whitney)
button_calculate.pack()

# Метка для вывода результатов
label_result = tk.Label(window, text="")
label_result.pack()

# Запуск цикла обработки событий
window.mainloop()
