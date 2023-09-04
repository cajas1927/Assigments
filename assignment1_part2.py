#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module Contains class and methods that stores and displays book title and author."""


class Book(object):
    """
    Attributes:
        author (str): Book Author.
        title (str): Book title.
    """
    author = ''
    title = ''

    def __init__(self, author, title):
        """
        Args:
            author (str): Author Name.
            title (str): Book name title.

        Returns:
            None

        Examples:
        >>> one = Book('Norton Juster','The Tollbooth Phantom')
        >>> one.display()
        >>> The Tollbooth Phantom Written by: Norton Juster
        """
        self.author = author
        self.title = title


    def display(self):
        """
        Args:
            None

        Returns:
            None

        Examples:
        >>> one.display()
        >>> The Tollbooth Phantom Written by: Norton Juster
        """
        print "%s Written by: %s" % (self.title, self.author)


if __name__ == '__main__':
    FIRST_BOOK = Book('John Steinbeck', 'Of Mice and Men')
    SECOND_BOOK = Book('Harper Lee', 'To Kill a Mockingbird')
    FIRST_BOOK.display()
    SECOND_BOOK.display()
