'''
Day 4
'''
#First Function to take seven datatype in funtion and print it

a=10
b=87.86
c="hello"
d=True
e=[2,4,6,8]
f=(1,3,5,7)
g={'name':"guru",'age': 21}

def firstfunc(int_val,float_val,string_val,bool_val,list_val,tuple_val,dict_val):
    print(f'integer value is:{int_val}')
    print(f'float value is:{float_val}')
    print(f'string value is:{string_val}')
    print(f'Boolean value is:{bool_val}')
    print(f'List value is:{list_val}')
    print(f'tuple value is:{tuple_val}')
    print(f'dict value is:{dict_val}')

firstfunc(a,b,c,d,e,f,g)


'''
Second Function to take a dictionary value and 
print its key & value using fprint
'''
def secondfunc(var):
    for key,value in var.items():
        print(f"Key is :{key} and Value is :{value}")

dict_a={'Name':"Guru",
        'place':'Kolkata',
        'Age':21}
    
secondfunc(dict_a)


'''
Third Function takes two number and return both the number in list
'''
first_num=1
second_num=2
def thirdfunc(x,y):
    return x,y

result=thirdfunc(first_num,second_num)
f,s=result
val_list=[f,s]
print(f'Value in list :{val_list}')