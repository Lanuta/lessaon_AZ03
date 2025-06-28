from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import matplotlib.pyplot as plt

# Настройка драйвера
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Список для цен
price_list = []

# Открываем сайт
driver.get("https://www.divan.ru/category/divany")
time.sleep(5)

# Подготовка CSV-файла
with open("divan_prices.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Название", "Цена (в рублях)"])

    # Перебираем первые 3 страницы каталога
    for page in range(1, 4):
        print(f"Обрабатывается страница {page}...")

        # Прокручиваем вниз постепенно (эмуляция прокрутки)
        for _ in range(5):
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(1)

        time.sleep(2)

        # Собираем товары
        titles = driver.find_elements(By.CSS_SELECTOR, "span[itemprop='name']")
        prices = driver.find_elements(By.CSS_SELECTOR, "span[data-testid='price']")

        for title, price in zip(titles, prices):
            try:
                price_clean = int(price.text.replace(" ", "").replace("руб.", "").strip())
                writer.writerow([title.text, price_clean])
                price_list.append(price_clean)
            except ValueError:
                continue  # Пропускаем, если цена некорректна

        # Переход на следующую страницу
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, "a[data-testid='pagination-forward']")
            next_btn.click()
            time.sleep(5)
        except:
            print("Следующая страница не найдена. Завершаем.")
            break

# Закрываем браузер
driver.quit()

# Вывод средней цены
if price_list:
    average_price = sum(price_list) / len(price_list)
    print(f"Средняя цена дивана: {int(average_price):,} руб.".replace(",", " "))
else:
    print("Не удалось собрать цены.")

# Строим гистограмму
plt.figure(figsize=(10, 6))
plt.hist(price_list, bins=10, color='lightgreen', edgecolor='black')
plt.title("Гистограмма цен на диваны (первые 3 страницы)")
plt.xlabel("Цена (руб.)")
plt.ylabel("Количество")
plt.grid(True)
plt.tight_layout()
plt.show()
