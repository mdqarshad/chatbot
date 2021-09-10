# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 12:47:46 2021

@author: smcha
"""

import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_OLD = "i am not that old as you"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response