import turtle

def draw_pythagoras_tree(t: turtle.Turtle, length: float, level: int):
    if level == 0:
        return

    # Малюємо стовбур (або гілку)
    t.forward(length)

    # Зберігаємо поточну позицію та напрямок
    position = t.pos()
    heading = t.heading()

    # Малюємо ліву гілку
    t.left(45)
    draw_pythagoras_tree(t, length * 0.7, level - 1)

    # Повертаємось до початкової позиції
    t.penup()
    t.setpos(position)
    t.setheading(heading)
    t.pendown()

    # Малюємо праву гілку
    t.right(45)
    draw_pythagoras_tree(t, length * 0.7, level - 1)

    # Повертаємось назад по стовбуру
    t.penup()
    t.setpos(position)
    t.setheading(heading)
    t.backward(length)
    t.pendown()

if __name__ == "__main__":
    import turtle

    # Ввід рівня рекурсії
    try:
        level = int(input("Введіть рівень рекурсії (наприклад, 6): "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        exit()

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("brown")
    t.speed(0)
    t.left(90)  # Повертаємо черепашку вгору

    # Стартова позиція внизу
    t.penup()
    t.goto(0, -250)
    t.pendown()

    draw_pythagoras_tree(t, length=100, level=level)

    screen.mainloop()