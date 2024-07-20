from iterdict import ParameterIterator

parameter_dictionary =  {'param1':[0, 1, 2],
                         'param2':'non-list is a fixed parameter',
                         'param3':['test this', 'and this']
}

params = ParameterIterator(parameter_dictionary)
for p in params:
    print (p)