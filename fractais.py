import turtle

# FUNÇÕES

# Função de desenhar o quadrado
def drawSquare(t, size):
  t.pd()
  t.begin_fill()
  t.fillcolor("purple")

  # desenho do quadrado
  for i in range(4):
    t.fd(size)
    t.right(90)

  t.end_fill()
  t.pu()

#funçao para desenhar o fractal do quadrado
def drawSquareFractal(t, size, step=40):
  # retorna quando acabar o número de passos ou quando o quadrado fica muito pequeno
  if step <= 0 or size < 5:
    return

  # Desenha um quadrado
  drawSquare(t, size)
  t.fd(size * 0.7)
  # Gira o fractal
  t.lt(18)

  # Chama a propria função, só que com um tamanho menor (assim se tornando uma funçao recursiva)
  drawSquareFractal(t, size * 0.95, step - 1)

# função que desenha a fractal de estrla
def drawStarFractal(t, size):
  # retorna quando a estrela fica muito pequena
  if size < 12:
    return
  
  t.pencolor("blue")
  # Desenha a estrela
  for i in range(5):
    t.fd(size)

    # Chama a propria função, desenhando uma estrela menor
    drawStarFractal(t, size * 0.35)
    # Gira o fractal
    t.lt(144)


def treeFractal(t, size, angle, nivel):
  # retorna quando o nivel acabar ou quando o galho fica muito pequeno
  if nivel == 0 or size < 10:
    return

  #desenha o galho principal
  t.pd()
  t.pencolor("brown")
  t.fd(size)

  # desenho  dos outros ramos
  t.rt(angle)
  t.pencolor("green")
  treeFractal(t, size * 0.7, angle, nivel - 1)
  t.lt(angle)

  t.pencolor("green")
  treeFractal(t, size * 0.75, angle, nivel - 1)

  t.lt(angle)
  t.pencolor("green")
  treeFractal(t, size * 0.7, angle, nivel - 1)

  t.rt(angle)
  t.back(size)

# TURTLE

t = turtle.Turtle()
t.speed(0)
t.pu()

# Desenho do fractal de quadrados 
t.goto(-330, 20)
t.setheading(0)
drawSquareFractal(t, 55, 30)


# Desenho da fractal de estrelas
t.pu()
t.goto(170, -40)
t.setheading(0)
t.pd()
drawStarFractal(t, 120)


# Desenho da árvore fractal 
t.pu()
t.goto(0, -300)
t.setheading(90)
treeFractal(t, 80, 35, 5)


