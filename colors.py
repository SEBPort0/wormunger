WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRIGHTRED = (255, 0, 0)
RED = (155, 0, 0)
BRIGHTGREEN = (0, 255, 0)
GREEN = (0, 155, 0)
BRIGHTBLUE = (0, 0, 255)
BLUE = (0, 0, 155)
BRIGHTYELLOW = (255, 255, 0)
YELLOW = (155, 155, 0)
DARKGRAY = (40, 40, 40)
BRIGHTORANGE = (255, 265, 0)
ORANGE = (255, 165, 0)
BRIGHTVIOLET = (238, 230, 238)
VIOLET = (238, 130, 238)

if __name__ == "__main__":
    allColors = {"white": WHITE, "black": BLACK, "brigth_red": BRIGHTRED,
                 "red": RED, "bright_green": BRIGHTGREEN, "green": GREEN,
                 "bright_blue": BRIGHTBLUE, "blue": BLUE,
                 "bright_yellow": BRIGHTYELLOW, "yellow": YELLOW,
                 "dark_gray": DARKGRAY, "bright_orange": BRIGHTORANGE,
                 "orange": ORANGE, "bright_violet": BRIGHTVIOLET,
                 "violet": VIOLET}
    for color, rgb in allColors.items():
        print("{} = {}".format(color, rgb))
