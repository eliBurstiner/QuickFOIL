import pytholog as pl
from pyswip import *
import random
import string
from itertools import combinations

#bg = pl.KnowledgeBase("Background Knowledge");
#pe = pl.KnowledgeBase("Positive Examples");
#ne = pl.KnowledgeBase("Negative Examples");
#lr = pl.KnowledgeBase("Learned Rules");

prolog = Prolog()
#prolog.assertz("father(michael,john)")

foo = "B(Andrew, Jaco)"
#prolog.assertz(foo)


#prolog.assertz("fater(michael,john)")

#B = Functor("B", 1)



background = ["brother(Andrew, Jacob)",
    "brother(Jason, Noah)",
    "brother(Jacob, Andrew)",
    "brother(Noah, Jacob)",
    "brother(Owen, William)",
    "father(Daniel, Andrew)",
    "father(Jason, Jacob)",
    "father(Noah, Jacob)",
    "father(Noah, Justin)",
    "father(Jimmy, Jason)",
    "son(Daniel, June)",
    "son(Daniel, Jennifer)",
    "son(Daniel, Rachel)",
    "son(Daniel, Jason)",
    "son(John, William)",
    "son(Noah, Gwen)",
    "son(Jason, Sara)"]

for i in background:
    prolog.assertz(i)

positive = ["uncle(Daniel, Jacob)",
          "uncle(Jason, Andrew)",
          "uncle(Noah, Andrew)",
          "uncle(Daniel, William)"]

for i in positive:
    prolog.assertz(i)

negative = ["uncle(John, Jason)",
         "uncle(Noah, John)",
         "uncle(Jason, Justin)",
         "uncle(Noah, Justin)"]

def QuickFOIL(target, background, positive, negative):
    pos = positive.copy()
    learnedRules = []
    while(len(pos) > 0):
        neg = negative.copy()
        rule = target + " :- "
        while(len(neg) > 0):
            candidates = generateCandidates(rule, background)
            bestScore = 0
            bestCandidate = ""
            for candidate in candidates:
                if(score(candidate) > bestScoree):
                    bestCandidate = candidate
                    bestScore = score(candidate)
            rule = rule + bestCandidate
            coveredNeg = negCoverage(bestCandidate)
            for example in coveredNeg:
                neg.remove(example)
        learnedRules.append(rule)
        coveredPos = posCoverage(rule)
        for example in coveredPos(rule):
            pos.remove(example)
    return learnedRules

def generateCandidates(rule, background):
    variables = []
    for element in rule:
        if(element.isupper() and variables.count(element) == 0):
            variables.append(element)
    varFlag = 0
    while(not varFlag):
        newVar = random.choice(string.ascii_uppercase)
        if(variables.count(newVar) == 0):
            variables.append(newVar)
            varFlag = 1
    predicates = []
    arity = []
    for element in background:
        pred = element[0:element.index("(")]
        if(predicates.count(pred) == 0):
            predicates.append(pred)
            arity.append(element.count(",") + 1)

    for i in predicates:
        print(i)
    for i in arity:
        print(i)
    for i in variables:
        print (i)
    candidates = []
    i = 0
    while(i < len(predicates)):
        comb = combinations(variables, arity[i])
        for c in comb:
            candidate = predicates[i] + c
    return candidates

            
poop = generateCandidates("uncle(X, Y)", background)
for i in poop:
    print(i)

def score():
    return 0

def negCoverage(example):
    return 0

def posCoverag(rule):
    return 0
