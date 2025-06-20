from rich import print
import random
import matplotlib.pyplot as plt
from collections import Counter

# Імітую кидання кубиків, вношу це до двох змінних
rols_of_dice_1 = [random.randint(1, 6) for _ in range(1000000)]
rols_of_dice_2 = [random.randint(1, 6) for _ in range(1000000)]

# При кожному кидку кубика додаю значення і рахую суму цих значень
sums = [rols_of_dice_1[i] + rols_of_dice_2[i] for i in range(1000000)]
counter = Counter(sums)

# Обчислюю ймовірність кодної суми
probabilities = {}
for suma in counter:
    probabilities[suma] = round(counter[suma]/1000000, 4)

# Тепер побудуємо графік
x = sorted(probabilities.keys())
y = [probabilities[i] for i in x]

plt.bar(x, y)
plt.title("Ймлвіоність випадіння сум кубиків")
plt.xlabel("Сума")
plt.ylabel("Ймовірність")
plt.grid(True)
plt.show()

print("\n[bold yellow]Ймовірність випадіння сум кубиків:[/bold yellow]\n")
for suma in sorted(probabilities):
    print(f"[green]Сума {suma}:[/green] {probabilities[suma]}")