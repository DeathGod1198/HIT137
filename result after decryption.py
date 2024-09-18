global_variable = 100
my_dict = {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'}
def process_numbers():
 global global_variable # global variable should be inside the function.
 local_variable = 5 # local_variable should be inside the function.
 numbers= [1, 2, 3, 4, 5]# numbers should be inside the function.
 while local_variable > 0: # while loop shoule be inside the function.
   if local_variable % 2 == 0: # if should be inside the while loop.
     numbers.remove (local_variable)
   local_variable -= 1 # this is use to reduce the local_variable by 1 and should be inside while loop.
 print(numbers) #since our function doesn't take any parameter, we use print instead of return inside the function but before the while loop.
my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
process_numbers()  # we directly call variable without storing it in any variables.
def modify_dict():
 local_variable = 10 #this should be inside the modify_dict() function.
 my_dict['ke14'] = local_variable #this should be inside the modify_dict() function.
modify_dict() #function doesn't take any argument
def update_global():
 global global_variable
 global_variable += 10
update_global () # we need to call the function.
for i in range(5):
  print(i)
  i+= 1 # i should be smaller because we used smaller i in the above condition.
if my_set is not None and my_dict['ke14'] == 10: #name of dictionary is wrong.
    print("Condition met!")
if 5 not in my_dict:
 print("5 not found in the dictionary!")
print(global_variable)
print(my_dict)
print(my_set)
