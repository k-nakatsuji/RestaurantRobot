

class Robot(object):
    """Base model Robots"""
    def __init__(self) -> None:
        pass

    def say(self, words):
        print(words)

    def hello(self):
        # ここにはテンプレ読み出し
        self.say("Hello")


class RestaurantRobot(Robot):
    """OrderRobot"""

    def __init__(self) -> None:
        pass

    # 自己紹介と名前を尋ねる

    #



