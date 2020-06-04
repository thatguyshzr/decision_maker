# heed the decision of Python, the unbaised.
from random import choice
from flask import jsonify

def decision_maker(things_to_make_decision_on, out_of= 10):
    list_of_things= []
    thing_list= str(things_to_make_decision_on).split(',')
    thing_list= [i for i in thing_list if i]    # remove blank strings
    list_of_things= [choice(thing_list) for i in range(out_of)]

    return list_of_things

def decision_counter(list_of_things):
    count_of_things= dict( (l, list_of_things.count(l)) for l in list_of_things )
    
    return count_of_things
