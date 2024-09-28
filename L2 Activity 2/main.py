# This is the main file for L1 Activity 2
class Employee:
  
    def __init__(self):
        print('Employee created')
  
    def __del__(self):
        print("Destructor called")
  
def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj
  
print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')