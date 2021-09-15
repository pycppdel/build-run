"""


Object.py -> Base class for all Objects displayed in Build&Run

All Objects derive from this class

"""

from abc import ABC; abstractmethod

class Object(ABC):

    """
    Base class for all following Objects.

    :Attributes:

    -x: int
    -y: int
    -width: int
    -height: int #So far: x and y coordinate, also the width and height needed to determine the hitbox
    -visible: bool #if the object is visible
    -animated: bool #if the object will be animated e.g for blocks is unnecessary
    -sprites: list[] # list with all the sprites built like PROP00X describes
    -hitbox_off: bool # if the hitbox is toggled off
    -hitbox: list # list with all hitboxes for the scpecific object
    -draw_method: func # function object of the draw method


    :Methods:

    set_draw_method(func): bool #sets the draw_method
    draw(screen): void
    offset_hitbox_coords(x, y, width, height): bool #sets the coords for the hitbox to +VALUE
    """

    def __init__(self, x=0, y=0, width=0, height=0, visible=False, animated=False\
                 sprites=[], hitbox_off=True, hitbox=[], draw_method=None):

        #initializer for the base object
        #setting values

        #starting with coords
        self.x = x
        self.y = y

        #next:width and height
        self.width = width
        self.height = height

        #visible
        self.visible = visible

        #if it's animated
        self.animated = animated

        #sprites folder
        self.sprites = sprites

        #hitbox stuff
        self.hitbox_off = hitbox_off
        self.hitbox = hitbox

        #draw_method
        self.draw_method = draw_method

    """
    body for methods
    """

    def draw(self, screen):
        """
        draws the set function on the screen
        """
        self.draw_method(screen)

    def set_draw_method(self, method):
        """
        sets the own draw_method to method
        """
        self.draw_method = method

    def offset_hitbox_coords(self, x=0, y=0, width=0, height=0):
        """
        offsets the hitbox coords to the given value, if it is None it stays the same
        """
        #offseting
        for el in self.hitbox:
            #offsetting for each
            el.x += x
            el.y += y
            el.width += width
            el.height += height
