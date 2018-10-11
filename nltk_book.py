# -*- coding: utf-8 -*-
# Sumin Seo
# NLTK Book - 5장까지

# parsing tree

import nltk
from nltk import CFG
from nltk.tree import *
from pycorenlp import StanfordCoreNLP
from collections import defaultdict

# define grammar
def defgrammar():
    Grammar = nltk.CFG.fromstring("""S -> NP VP
    PP -> P NP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    Det -> 'an' | my
    N -> 'elephant' | 'pajamas'
    V -> 'shot'
    P -> in
    """)

    sent = "I shot an elephant".split()
    parser - nltk.ChartParser(Grammar)
    trees = parser.parse(sent)
    for tree in trees:
        print(tree)

def draw_parse_tree():
    dp1 = Tree('dp', [Tree('d', ['the']), Tree('np', ['dog'])])
    dp2 = Tree('dp', [Tree('d', ['the']), Tree('np', ['cat'])])
    vp = Tree('vp', [Tree('v', ['chased']), dp2])
    print(tree)
    print(tree.pformat_latex_gtree())

def parsing_result():
    text = """I shot an elephant. The dog chased the cat. School go to boy."""
    res = nlp.annotate(text, properties =
    {'annotator':'tokenize.ssplit.pos.deparse.parse', 'outputFormat':'json'})
    print(res['sentence'][0]['parse'])
    print(res['sentence'][2]['parse'])

ptint("Parsing result as per definied grammar")
defgrammar()
print("Drawing parse tree")
draw_parse_tree()
print("Standford Parser result")
parsing_result