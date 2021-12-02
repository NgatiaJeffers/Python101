import ball

class BowlingBall(ball.Ball):

    def roll(self):
        print(f'You are rolling the {self.ball_type} ball')

    def bounce(self):
        print(f"The {self.ball_type} can't bounce ")

if __name__ == '__main__':
    ball = BowlingBall('green', 10, 15, 'bowling')
    ball.roll()

    ball.bounce()
    ball.bounce()