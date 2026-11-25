import cv2
from datetime import datetime

def log(name, status):
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    with open("Lab2_Media/logs/history.txt", "a", encoding="UTF-8") as f:
        f.write(f"[{now}] Файл: {name} | Фильтр: Гаусс + Серый мир | Статус: {status}\n")

def gauss_filter(img):
    return cv2.GaussianBlur(img, (7, 7), 0)

def gray_world(img):
    wb = cv2.xphoto.createGrayworldWB()
    return wb.balanceWhite(img)

name = input("Введите имя файла: ")
path = "Lab2_Media/data/input/" + name

try:
    open(path, "rb").close()  # проверяем, что файл есть и его можно читать
except FileNotFoundError:
    print("Ошибка: Файл не найден")
    log(name, "Файл не найден")
except PermissionError:
    print(f"Ошибка: Нет прав на чтение файла")
    log(name, "Ошибка доступа")
else:
    img = cv2.imread(path)

    if img is None:
        print("Ошибка: Не удалось открыть файл как изображение")
        log(name, "Ошибка чтения")
    else:
        img = gauss_filter(img)
        img = gray_world(img)
        cv2.imwrite("Lab2_Media/data/output/result.jpg", img)
        print("Успешно: Результат сохранён")
        log(name, "Успешно")