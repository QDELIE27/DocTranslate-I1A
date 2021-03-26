"""Fourchelang library for snakes lovers!"""


import re

#: The name of the snake
SNAKE_NAME = "SssquentinSssnake"


def translate(text):
    """Translate the given text to Parseltongue.

    :param str text: The text to translate.

    :returns: the translated text.
    :rtype: str

    >>> translate("Hello!")
    'sssss!'
    >>> translate("I am a sssnake!")
    's ss s sssssss!'
    """
    return re.sub(r"[\w\d]", "s", text)


class Snake:

    """This is a snake.

    :param str name: The snake's name.
    """

    def __init__(self, name):
        """The constructor."""
        self.name = name

    def move(self, x, y):
        """Moves the snake to given position.

        .. WARNING::

            Be careful to not tie knots when moving the snake!

        :param int x: The x position where move to.
        :param int y: The y position where move to.
        """
        pass

    def speak(self):
        """Makes the snake speak."""
        return translate("Hello, I'm a ssssssnake!")
