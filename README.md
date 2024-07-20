# iterdict
Cartesian Product Iterators from dictionaries

## Installation

Directly from the GitHub repository:

    pip install git+https://github.com/tiagoft/iterdict.git@main


## What is this?

I frequently encountered the challenge of managing numerous parameters within an algorithm. Understanding how these parameters influence behavior required a thorough exploration of their combinations, akin to a grid search. To address this, I developed `ParameterIterator`.

`ParameterIterator` is designed to take a dictionary where some entries are lists. It iterates over these lists in a Cartesian product manner, generating all possible combinations. During each iteration, it yields a dictionary with the respective list entries, facilitating an exhaustive parameter exploration.

## Example

    from iterdict import ParameterIterator

    parameter_dictionary =  {'param1':[4, 3, 2, 1],
                            'param2':'non-list is a fixed parameter',
                            'param3':['test this', 'and this']
                        }
    params = ParameterIterator(parameter_dictionary)
    for p in params:
        print (p)
    
Result:

    {'param1': 0, 'param2': 'non-list is a fixed parameter', 'param3': 'test this'}
    {'param1': 0, 'param2': 'non-list is a fixed parameter', 'param3': 'and this'}
    {'param1': 1, 'param2': 'non-list is a fixed parameter', 'param3': 'test this'}
    {'param1': 1, 'param2': 'non-list is a fixed parameter', 'param3': 'and this'}
    {'param1': 2, 'param2': 'non-list is a fixed parameter', 'param3': 'test this'}
    {'param1': 2, 'param2': 'non-list is a fixed parameter', 'param3': 'and this'}

