from rich import print

class Item:
    def __init__(self, cost, calories):
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost

def greedy_algorithm(items: dict, budget: int):
    food_list = [(name, Item(data["cost"], data["calories"])) for name, data in items.items()]
    food_list.sort(key = lambda x: x[1].ratio, reverse=True)
    total_calories = 0
    selected_food = []
    for food in food_list:
        if budget >= food[1].cost:
            budget -= food[1].cost
            total_calories +=food[1].calories
            selected_food.append(food[0])
    return total_calories, selected_food

def dynamic_programming(items: dict, budget: int):
    # Крок 1: Готуб списки 
    food_list = list(items.keys())
    cost = [items[food]["cost"] for food in food_list]
    calories = [items[food]["calories"] for food in food_list]
    n = len(food_list)

    # Крок 2: Ініціалізація таблиці
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Крок 3: Побудова таблиці DP
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if cost[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Крок 4: Визначення обраних страв
    w = budget
    selected_food = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_food.append(food_list[i - 1])
            w -= cost[i - 1]

    selected_food.reverse()  # Щоб список був у правильному порядку
    total_calories = dp[n][budget]

    return selected_food, total_calories
    



if __name__ == "__main__":
    items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
    budget = 110

    greed, foods = greedy_algorithm(items, budget)
    print("\n===Розвязування за допомогою жадібного алгоритму===")
    print(f"[bold green]Максимальна кількість калорійх: [/bold green]\n{greed}")
    print(f"\n[bold yellow]Список страв:[/bold yellow]\n{foods}")

    dynamic, eats = dynamic_programming(items, budget)
    print("\n===Розвязування за допомогою динамічного===")
    print(f"[bold green]Максимальна кількість калорійх: [/bold green]\n{eats}")
    print(f"\n[bold yellow]Список страв:[/bold yellow]\n{dynamic}")

    
