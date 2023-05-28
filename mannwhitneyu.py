from scipy.stats import mannwhitneyu

# Пример данных двух выборок
group1 = [1, 2, 3, 4, 5]
group2 = [2, 4, 6, 8, 10]

# Выполняем тест Манна-Уитни
statistic, p_value = mannwhitneyu(group1, group2)

# Выводим результаты
print("Статистика теста Манна-Уитни:", statistic)
print("p-значение:", p_value)