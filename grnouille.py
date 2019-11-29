# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from pyDatalog import pyDatalog
pyDatalog.clear()
pyDatalog.create_terms('X, eatFiles, green, yellow, croakes, chirps, sings, canary, frog, P')

pyDatalog.load("""
""")

frog(X) <= croakes(X) & eatFiles(X)
canary(X) <= chirps(X) & sings(X)
green(X) <= frog(X)
yellow(X) <= canary(X)


pyDatalog.assert_fact('croakes', 'fritz')
pyDatalog.assert_fact('eatFiles', 'fritz')

query = 'frog(X)'
answers = pyDatalog.ask(query).answers 
print(answers)