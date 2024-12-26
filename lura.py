import turtle

# Fungsi untuk menggambar hati
def draw_heart():
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    turtle.circle(-112, 200)
    turtle.left(120)
    turtle.circle(-112, 200)
    turtle.forward(224)
    turtle.end_fill()

# Fungsi untuk menggambar bunga
def draw_flower():
    turtle.color('magenta')
    turtle.begin_fill()
    for _ in range(36):  # Menggambar 36 petal
        turtle.circle(100, 60)  # Menggambar setengah lingkaran
        turtle.left(120)
        turtle.circle(100, 60)  # Menggambar setengah lingkaran
        turtle.left(100)  # Memutar untuk petal berikutnya
    turtle.end_fill()

# Fungsi untuk menulis nama
def write_name():
    turtle.penup()
    turtle.goto(0, -50)  # Pindah ke posisi untuk menulis nama
    turtle.color('black')
    turtle.write("Riska Herliana", align="center", font=("Arial", 24, "bold"))

# Mengatur layar
turtle.speed(3)
turtle.bgcolor('white')

# Menggambar hati
turtle.penup()
turtle.goto(-100, 0)  # Pindah ke posisi untuk menggambar hati
turtle.pendown()
draw_heart()

# Menggambar bunga
turtle.penup()
turtle.goto(100, 0)  # Pindah ke posisi untuk menggambar bunga
turtle.pendown()
draw_flower()

# Menulis nama
write_name()

# Menyelesaikan gambar
turtle.hideturtle()
turtle.done()