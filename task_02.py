#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""w6 synthesizing task 02."""


def prepare_email(appointments):
    """Email that reminds people of their
    apointments.

    Args:
        Appointments(list): a list of two-item tuples
        that displays name and their apointment.

    Returns:
        email(str): text that shows client apointment.

    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['Dear Jen,\nI look forward to meeting with you on 2015.
        \nBest,\nMe','Dear Max,\nI look forward to meeting
        you on March 3.\nBest\nMe']
    """
    # email = []
    # email_txt = 'Dear {},\nI look forward to meeting' +
    #            ' with you on {}.\nBest,\nMe'
    # for people in appointments:
    #   email.append(email_txt.format(people[0], people[1]))
    # return email

    email_txt = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    return [email_txt.format(appointment[0], appointment[1])
            for appointment in appointments]
