#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""w6 synthesizing taks. """


def get_party_stats(families, table_size=6):
    """This function takes 2 parameters which are families and table_size.

    Args:
        families(list): lists families.
        table_size(int): shows the max number of seats at each table.

    Return:
        a tuple that resturns the total number of guests and tables.


    Example:
         >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack'
         'Janis']])(6, 3)
         >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack'
         'Janis']],2)(6, 4)
    """
    total_guests = 0
    total_tables = 0
    for members in families:
        family = len(members)
        total_guests += family
        total_tables += -(-family//table_size)

    return (total_guests, total_tables)
