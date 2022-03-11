import cv2
import time
import random
import numpy as np
import pandas as pd

TILE_SIZE = 32

MARKET = """
##WWWWWWWWWWWWWWW##
#tttttttttttttttttG
rRtDeeDtSssStFbaFt#
dRtDmmDtSppStFbaFt#
rRtDeeDtSssStFbaFt#
dRtDmmDtSppStFbaFt#
rRtDeeDtSssStFbaFt#
rRtttttttttttttttt#
CCccCCccCCccCCtttt#
##tttttttttttttttt#
##tttttttttttttttt#
##EEEEEEEEEEEEEEE##
""".strip()


class SupermarketMap:
    """Visualizes the supermarket background"""

    def __init__(self, layout, tiles):
        """
        layout : a string with each character representing a tile
        tiles   : a numpy array containing all the tile images
        """
        self.tiles = tiles
        # split the layout string into a two dimensional matrix [['#','#',..],['#','#',.]]
        self.contents = [list(row) for row in layout.split("\n")]
        self.ncols = len(self.contents[0])
        self.nrows = len(self.contents)
        # create a 3d np.zeros image with shape (384, 576, 3)
        self.image = np.zeros(
            (self.nrows*TILE_SIZE, self.ncols*TILE_SIZE, 3), dtype=np.uint8
        )
        self.prepare_map()

    def extract_tile(self, row, col):
        """extract a tile array from the tiles image"""
        # we get tile array inserting the row and col in the tiles.png where our tile is
        y = row*TILE_SIZE
        x = col*TILE_SIZE
        return self.tiles[y:y+TILE_SIZE, x:x+TILE_SIZE]

    def get_tile(self, char):
        """returns the array for a given tile character"""
        if char == "#":
            return self.extract_tile(0, 0)
        elif char == "G":
            return self.extract_tile(7, 3)
        elif char == "C":
            return self.extract_tile(2, 8)
        elif char == "b":
            return self.extract_tile(0, 4)
        elif char == "a":
            return self.extract_tile(5, 4)
        elif char == "s":
            return self.extract_tile(5, 9)
        elif char == "p":
            return self.extract_tile(6, 9)
        elif char == "e":
            return self.extract_tile(-2, -5)
        elif char == "m":
            return self.extract_tile(-4, 6)
        elif char == "d":
            return self.extract_tile(3, -3)
        elif char == "r":
            return self.extract_tile(-3, -3)
        elif char == "W":
            return self.extract_tile(0, 7)
        elif char == "E":
            return self.extract_tile(-3, -6)
        else:
            return self.extract_tile(1, 2)

    def prepare_map(self):
        """prepares the entire image as a big numpy array"""
        # this for loops goes through the MARKET char's layout, and it creates the image
        for row, line in enumerate(self.contents):
            for col, char in enumerate(line):
                # bm give back a real tile from tiles.png
                bm = self.get_tile(char)
                y = row*TILE_SIZE
                x = col*TILE_SIZE
                self.image[y:y+TILE_SIZE, x:x+TILE_SIZE] = bm

    def draw(self, frame):
        """
        draws the image into a frame
        """
        ###
        frame[0:self.image.shape[0], 0:self.image.shape[1]] = self.image

    def write_image(self, filename):
        """writes the image into a file"""
        cv2.imwrite(filename, self.image)


class Customer_map:

    def __init__(self, supermarket, avatar, row, col):
        """
        supermarket: A SuperMarketMap object
        avatar : a numpy array containing a 32x32 tile image
        row: the starting row
        col: the starting column
        """

        self.supermarket = supermarket
        self.avatar = avatar
        self.row = row
        self.col = col

    def draw(self, frame):
        x = self.col * TILE_SIZE
        y = self.row * TILE_SIZE
        frame[y:y+TILE_SIZE, x:x+TILE_SIZE] = self.avatar

    def move(self):
        states = ['checkout', 'dairy', 'drinks', "fruit", 'spices']
        dairy = [(2, 3), (2, 6), (3, 3), (3, 6), (4, 3),
                 (4, 6), (5, 3), (5, 6), (6, 3), (6, 6)]
        fruits = [(2, 13), (2, 16), (3, 13), (3, 16), (4, 13),
                  (4, 16), (5, 13), (5, 16), (6, 13), (6, 16)]
        drinks = [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
        spices = [(2, 8), (2, 11), (3, 8), (3, 11), (4, 8),
                  (4, 11), (5, 8), (5, 11), (6, 8), (6, 11)]
        checkout = [(8, 2), (8, 3), (8, 6), (8, 7), (8, 10), (8, 11)]

        state = random.choice(states)

        if state == 'fruit':
            self.row, self.col = random.choice(fruits)

        if state == 'checkout':
            self.row, self.col = random.choice(checkout)

        if state == 'spices':
            self.row, self.col = random.choice(spices)

        if state == 'dairy':
            self.row, self.col = random.choice(dairy)

        if state == 'drinks':
            self.row, self.col = random.choice(drinks)


if __name__ == "__main__":

    # we are creating a bigger zeros array as background for our image
    background = np.zeros((500, 700, 3), np.uint8)
    tiles = cv2.imread("tiles.png")

    market = SupermarketMap(MARKET, tiles)
    customer_map = Customer_map(market, market.extract_tile(7, 0), 1, 18)
    # df = pd.read_csv("Supermarket_01.csv", index_col=1, parse_dates=True)
    # list_of_avatars = []
    # possible_avatar_pos = [(7, 0), (-2, -1), (-3, -1), (-4, -1), (-5, -1)]
    # for i in list(df.customer_name.unique()):
    #     customer = Customer_map(market, i, market.extract_tile(random.choice[possible_avatar_pos]), 1, 18)
    #     list_of_avatars.append(customer)

    while True:
        # for c_n in df
        #     for c in list_of_avatars:

        frame = background.copy()
        market.draw(frame)
        customer_map.draw(frame)

        time.sleep(2)
        customer_map.move()

        # if customer in

        # https://www.ascii-code.com/
        key = cv2.waitKey(1)

        if key == 113:  # 'q' key
            break

        cv2.imshow("frame", frame)

    cv2.destroyAllWindows()

    market.write_image("supermarket.png")
