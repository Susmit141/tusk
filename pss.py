# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 00:56:04 2019

@author: SUSHMIT
"""

def is_palindrome_v1(s):
    """ (str) -> bool
    Return True if and only if s is a palindrome.
    >>> is_palindrome_v1('noon)
    True
    >>> is_palindrome_v1('dented')
    False
    """
    def reverse(s):
        """  (str) -> str
        Return a revered version of s.
        >>> reverse('hello')
        'olleh'
        >>>reverse('a')
        'a'
        """
        rev= ''
        # For each character in s,
    