import roboter.src.robot as robot

jojo = robot.RestaurantRobot()

jojo.hello()

while True:
    # print("Hello")
    text = input("please your message")

    if text == "fin":
        break
