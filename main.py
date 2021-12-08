from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PingPongPaddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self,ball):
        if(self.collide_widget(ball)):
            ball.velocity_x *=-1
            ball.velocity_x +=1
            if(ball.velocity_y > 0 ):
                ball.velocity_y +=1
            else:
                ball.velocity_y -=1



class PingPongBall(Widget):
    velocity_x= NumericProperty(0)
    velocity_y= NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    def move(self):
        self.pos = Vector(self.velocity) + self.pos

class PingPongGame(Widget):
    ball = ObjectProperty(None)
    paddle_left=ObjectProperty(None)
    paddle_right=ObjectProperty(None)
    def serve_ball(self):
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))

    def update(self, dt):
        self.ball.move()
        if(self.ball.y<0) or (self.ball.y > self.height-self.ball.height):
            self.ball.velocity_y *=-1
        if (self.ball.x < 0):
            self.ball.velocity_x *= -1
            self.paddle_left.score +=1
        elif (self.ball.x > self.width - self.ball.width):
            self.ball.velocity_x *= -1
            self.paddle_right.score += 1
        if (self.paddle_left.y<=0):
            self.paddle_left.y=0
        if (self.paddle_left.y >= self.height-self.paddle_left.height):
            self.paddle_left.y = self.height-self.paddle_left.height
        if (self.paddle_right.y <=0):
            self.paddle_right.y=0
        if (self.paddle_right.y >= self.height-self.paddle_left.height):
            self.paddle_right.y = self.height-self.paddle_left.height
        self.paddle_left.bounce_ball(self.ball)
        self.paddle_right.bounce_ball(self.ball)
    def on_touch_move(self, touch):
        if (touch.x < self.width / 1 /4):
            self.paddle_left.center_y = touch.y
        if (touch.x > self.width * 3/4):
            self.paddle_right.center_y = touch.y

class PingPong(App):
    def build(self):
        game = PingPongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/100.0)
        return game

PingPong().run()