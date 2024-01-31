import tkinter as tk
import random


class Jeu2048:

  def __init__(self, rows, cols, objectif):
    self.rows = rows
    self.cols = cols
    #Objectif de fin 
    self.objectif = objectif
    self.score = 0
    self.board = [[0] * cols for _ in range(rows)]
    self.partie_finie= False
    self.won = False

    self.window = tk.Tk()
    self.window.title("2048")
    self.frame = tk.Frame(self.window)
    self.frame.pack()

    self.buttons = [[None] * cols for _ in range(rows)]
    self.create_grid()
    self.generer_case()
    self.generer_case()
    self.update_plateau()

  def create_grid(self):
    for i in range(self.rows):
      for j in range(self.cols):
        button = tk.Button(self.frame,
                           text="",
                           width=5,
                           height=2,
                           font=("Helvetica", 20, "bold"))
        button.grid(row=i, column=j, padx=5, pady=5)
        self.buttons[i][j] = button

  def update_plateau(self):
    for i in range(self.rows):
      for j in range(self.cols):
        value = self.board[i][j]
        text = str(value) if value != 0 else ""
        color = self.get_couleur_case(value)
        self.buttons[i][j].configure(text=text, bg=color)

  def get_couleur_case(self, value):
    colors = {
        0: "#CDC1B4",
        2: "#EEE4DA",
        4: "#EDE0C8",
        8: "#F2B179",
        16: "#F59563",
        32: "#F67C5F",
        64: "#F65E3B",
        128: "#EDCF72",
        256: "#EDCC61",
        512: "#EDC850",
        1024: "#EDC53F",
        2048: "#EDC22E",
    }
    return colors.get(value, "#CDC1B4")

  def generer_case(self):
    empty_cells = [(i, j) for i in range(self.rows) for j in range(self.cols)
                   if self.board[i][j] == 0]
    if empty_cells:
      i, j = random.choice(empty_cells)
      self.board[i][j] = 2 if random.random() < 0.9 else 4

  def move(self, direction):
    if self.partie_finie or self.won:
      return

    if direction == "left":
      self.move_left()
    elif direction == "right":
      self.move_right()
    elif direction == "up":
      self.move_up()
    elif direction == "down":
      self.move_down()

    self.update_plateau()
    self.generer_case()

    if self.check_fin_partie():
      self.partie_finie = True
      self.afficher_message("Fin de partie")
    if self.objectif in [tile for row in self.board for tile in row]:
      self.won = True
      self.afficher_message("Vous avez gagné, vous avez atteint votre objetif de " + self.objectif )
      print("Kepp going you gonna win the CSGAMES!!!")

  def move_left(self):
    for i in range(self.rows):
      self.board[i] = self.fusion(self.board[i])

  def move_right(self):
    for i in range(self.rows):
      self.board[i] = self.fusion(self.board[i][::-1])[::-1]

  def move_up(self):
    self.board = [list(x) for x in zip(*self.board)]
    for i in range(self.cols):
      self.board[i] = self.fusion(self.board[i])
    self.board = [list(x) for x in zip(*self.board)]

  def move_down(self):
    self.board = [list(x) for x in zip(*self.board)]
    for i in range(self.cols):
      self.board[i] = self.fusion(self.board[i][::-1])[::-1]
    self.board = [list(x) for x in zip(*self.board)]

  def fusion(self, line):
    result = [0] * len(line)
    j = 0
    for i in range(len(line)):
      if line[i] != 0:
        if result[j] == 0:
          result[j] = line[i]
        elif result[j] == line[i]:
          result[j] *= 2
          self.score += result[j]
          j += 1
        else:
          j += 1
          result[j] = line[i]
    return result


  # Condition de fin 
  def check_fin_partie(self):
    for i in range(self.rows):
      for j in range(self.cols):
        if self.board[i][j] == 0:
          return False

    for i in range(self.rows):
      for j in range(self.cols - 1):
        if self.board[i][j] == self.board[i][j + 1]:
          return False

    for i in range(self.rows - 1):
      for j in range(self.cols):
        if self.board[i][j] == self.board[i + 1][j]:
          return False

    return True

  def afficher_message(self, message):
    popup = tk.Toplevel()
    popup.title("2048")
    label = tk.Label(popup, text=message, font=("Helvetica", 20, "bold"))
    label.pack(padx=20, pady=20)
    restart_button = tk.Button(popup,
                               text="Restart",
                               command=self.recommencer)
    restart_button.pack(pady=10)

  def recommencer(self):
    self.board = [[0] * self.cols for _ in range(self.rows)]
    self.score = 0
    self.partie_finie= False
    self.won = False
    self.generer_case()
    self.generer_case()
    self.update_plateau()

  def run(self):
    self.window.bind("<Left>", lambda event: self.move("left"))
    self.window.bind("<Right>", lambda event: self.move("right"))
    self.window.bind("<Up>", lambda event: self.move("up"))
    self.window.bind("<Down>", lambda event: self.move("down"))
    self.window.mainloop()


if __name__ == "__main__":
  rows = int(input("Nombre de lignes : "))
  cols = int(input("Nombre de colonnes : "))
  objectif = int(input("Objectif de victoire (ex. 2048) : "))
  game = Jeu2048(rows, cols, objectif)
  game.run()
