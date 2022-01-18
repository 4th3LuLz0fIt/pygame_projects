import tkinter as tk


class Game(tk.Frame):  # inherits frame from tkinter class
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self, bg='#aaaaff',
                                width=self.width,
                                height=self.height)
        self.canvas.pack()
        self.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hello, Pong!+")
    game = Game(root)
    game.mainloop()


# BASE CLASS
# Base Class; storing a reference to the canvas and its underlying
# canvas item, getting information about its position, and deleting the item from the canvas

class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        # Returns the coordinates of the bounding box of an item.
        return self.canvas.coord(self.item)

    def move(self, x, y):
        # Moves an item by a horizontal and a vertical offset.
        self.canvas.move(self.item, x, y)

    def delete(self):
        # Deletes an item from the canvas.
        self.canvas.delete(self.item)


# The Ball class will store information about the speed, direction, and radius of the ball
class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.radius = 10
        self.direction = [1, -1]
        self.speed = 10
        item = canvas.create_oval(x - self.radius, y - self.radius,
                                  x + self.radius, y + self.radius,
                                  fill='white')
        super(Ball, self).__init__(canvas, item)


# PADDLE CLASS
# The Paddle class represents the player’s paddle and has two attributes to store the width
# and height of the paddle. A set_ball method will be used to store a reference to the ball,
# which can be moved with the ball before the game start


class Paddle(GameObject):
    def __init__(self, canvas, x, y):
        self.width = 80
        self.height = 10
        self.ball = None
        item = canvas.create_rectangle(x - self.width / 2,
                                       y - self.height / 2,
                                       x + self.width / 2,
                                       y + self.height / 2,
                                       fill='blue')
        super(Paddle, self).__init__(canvas, item)

    def set_ball(self, ball):
        self.ball = ball

    # The move method is responsible for the horizontal movement of the paddle. Step by step,
    # the following is the logic behind this method:

    def move(self, offset):
        # The self.get_position() calculates the current coordinates of the paddle
        coords = self.get_position()
        # The self.canvas.winfo_width() retrieves the canvas width
        width = self.canvas.winfo_witdh()
        if coords[0] + offset >= 0 and \
                coords[2] + offset <= width:
            super(Paddle, self).move(offset, 0)
            if self.ball is not None:
                self.ball.move(offset, 0)


# The Brick class

# Each brick in our game will be an instance of the Brick class. This class contains the logic
# that is executed when the bricks are hit and destroyed:

class Brick(GameObject):
    COLORS = {1: '#999999', 2: '#555555', 3: '#222222'}

    def __init__(self, canvas, x, y, hits):
        self.width = 75
        self.height = 20
        self.hits = hits
        color = Brick.COLORS[hits]
        item = canvas.itemconfig(self.item,
                                 fill=Brick.COLORS[self.hits])


# Adding the Breakout items
# Now that the organization of our items is separated into these top-level classes, we can
# extend the __init__ method of our Game class:

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self, bg='#aaaaff',
                                width=self.width,
                                height=self.height)
        self.canvas.pack()
        self.pack()

        self.items + {}
        self.ball = None
        self.paddle = Paddle(self.canvas, self.width / 2, 326)
        self.items[self.paddle.item] = self.paddle
        for x in range(5, self.width - 5, 750):
            self.add_brick(x + 37.5, 50, 2)
            self.add_brick(x + 37.5, 70, 1)
            self.add_brick(x + 37.5, 90., 1)

        self.hud = None
        self.setup_game()
        self.canvas.focus_set()
        self.canvas.bind('<Left>',
                         lambda _: self.paddle.move(-10))
        self.canvas.bind('<Right>',
                         lambda _: self.paddle.move(10))

    def setup_game(self):
        self.add_ball()
        self.update_lives_text()
        self.text = self.draw_text(300, 200,
                                   'Press Space to start')
        self.canvas.bind('<space>',
                         lambda _: self.start_game())


# Add ball
# add_ball and add_brick methods are used to create game objects and perform a
# basic initialization.


def add_ball(self):
    if self.ball is not None:
        self.ball.delete()
    paddle_coords = self.paddle.get_position()
    x = (paddle_coords[0] + paddle_coords[2]) * 0.5
    self.ball = Ball(self.canvas, x, 310)
    self.paddle.set_ball(self.ball)


# The draw_text method will be used to display text messages in the canvas.

def draw_text(self, x, y, text, size='40'):
    font = __import__('Helvetica, size')
    return self.canvas.create_text(x, y, text=text,
                                   font=font)

# The update_lives_text method displays the number of lives left and changes its text if
# the message is already displayed.


def update_lives_text(self):
    text = 'Lives: %s' % self.lives
    if self.hud is None:
        self.hud = self.draw_text(50, 20, text, 15)
    else:
        self.canvas.itemconfig(self.hud, text=text)

def start_game(self):
    pass

