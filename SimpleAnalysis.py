import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.random.randint(-10000, 10000, size=1000)
series = pd.Series(data)

min_value = series.min()
num_duplicates = series.duplicated().sum()
max_value = series.max()
sum_value = series.sum()
std_deviation = series.std()

print("Минимальное значение: ", min_value)
print("Количество повторяющихся значений: ", num_duplicates)
print("Максимальное значение: ", max_value)
print("Сумма чисел: ", sum_value)
print("Среднеквадратическое отклонение: ", std_deviation)

series.to_csv("data.csv", index=False)

plt.figure(figsize=(8, 6))
plt.plot(series)
plt.title("Линейный график данных")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.show()

rounded_series = series.round(-2)
plt.figure(figsize=(8, 6))
plt.hist(rounded_series, bins='auto')
plt.title("Гистограмма данных")
plt.xlabel("Значение (округленное до сотен)")
plt.ylabel("Частота")
plt.show()

df = pd.DataFrame({"Data": series})
df["Sorted Ascending"] = df["Data"].sort_values(ascending=True)
df["Sorted Descending"] = df["Data"].sort_values(ascending=False)

plt.figure(figsize=(8, 6))
plt.plot(df["Sorted Ascending"], label="Sorted Ascending")
plt.plot(df["Sorted Descending"], label="Sorted Descending")
plt.title("Линейный график отсортированных значений")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.legend()
plt.show()

