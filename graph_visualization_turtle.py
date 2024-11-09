import turtle
import math

def draw_graph(adj_matrix, labels):
    num_nodes = len(adj_matrix)
    
    # Создаем окно Turtle
    screen = turtle.Screen()
    screen.title("Граф в форме круга")
    
    # Создаем черепашку для рисования
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    
    # Вычисляем координаты узлов по окружности
    radius = 200
    angle_step = 360 / num_nodes
    positions = []
    
    for i in range(num_nodes):
        angle = math.radians(i * angle_step)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        positions.append((x, y))
        
        # Рисуем узел
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(30, "lightblue")
        
        # Добавляем метку узла
        t.penup()
        t.goto(x + 10, y + 10)
        t.write(labels[i], align="center", font=("Arial", 12, "bold"))
    
    # Рисуем рёбра
    for i in range(num_nodes):
        for j in range(i, num_nodes):
            if adj_matrix[i][j] == 1:
                t.penup()
                t.goto(positions[i])
                t.pendown()
                t.goto(positions[j])
    
    # Завершаем выполнение
    screen.mainloop()

def input_matrix_and_labels():
    print("Введите количество узлов графа:")
    n = int(input())
    
    print("Введите матрицу смежности построчно, разделяя числа пробелами (например, для строки '0 1 0'):")
    adj_matrix = []
    for i in range(n):
        row = list(map(int, input(f"Строка {i+1}: ").split()))
        if len(row) != n:
            raise ValueError("Каждая строка матрицы должна содержать ровно n элементов.")
        adj_matrix.append(row)
    
    print("Введите метки для узлов (по одной на строку):")
    labels = {}
    for i in range(n):
        label = input(f"Метка для узла {i}: ")
        labels[i] = label
    
    return adj_matrix, labels

# Ввод данных
adj_matrix, labels = input_matrix_and_labels()

# Построение графа
draw_graph(adj_matrix, labels)
