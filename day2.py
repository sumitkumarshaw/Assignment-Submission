#DAY 2 Assignment
'''
Declaring SEVEN Different datatype 
'''
first_int=5 
second_float=2.2
third_bool=True
fourth_list=list()
fourth_list.append(3)
fourth_list.append(5)
fourth_list.append(7)
fourth_list.append(9)
fifth_tuple=(1,2,3,4,5)
sixth_dict=dict()
sixth_dict['name']='Day 2 Assignment'
seventh_set={1,2,3,4,5}

"""
Print Statement in simpler one
"""

print("integer value:",first_int,"\nfloat value:",second_float,
      "\nboolean value:",third_bool,"\nlist value:",fourth_list,
      "\ntuple value:",fifth_tuple,"\ndictionary value:",sixth_dict,
      "\nset value:",seventh_set)

'''
print statement in %s
'''

print("\n integer value:%s \n float value:%s \n boolean value:%s \n list_value:%s \n tuple_value:%s \n dict_value:%s \n set_value:%s"
      %(first_int,second_float,third_bool,fourth_list,fifth_tuple,sixth_dict,seventh_set))

'''
print statement in .format
'''

print("\n integer value:{} \n float value:{} \n boolean value:{} \n list_value:{} \n tuple_value:{} \n dict_value:{} \n set_value:{}"
      .format(first_int,second_float,third_bool,fourth_list,fifth_tuple,sixth_dict,seventh_set))

'''
print statement f string
'''

print(f'\n integer value:{first_int} \n float value:{second_float} \n boolean value:{third_bool} \n list_value:{fourth_list} \n tuple_value:{fifth_tuple} \n dict_value:{sixth_dict} \n set_value:{seventh_set}')
