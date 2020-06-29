# Decorators
import time
from datetime import datetime

def dec_capatilize(func):
    def make_cap(name):
        print("In Dec Inner")
        upper_name = name.upper()
        #print(name.upper())
        return func(upper_name)
    return make_cap

def calculate_time(func):
    print("in calculate_time")
    def calc(*args):
        print("in inner func calc()")
        start_time = time.time()
        print("start time : ",start_time)
        func()
        end_time = time.time()
        print("end_time  : ", end_time)
        exec_time = end_time - start_time
        print("Time for Execution: ",exec_time)
        return exec_time
    return calc


#dec_capatilize
@calculate_time
def enter_name(name):
    print("Welcome "+ name +"!!!")
    now = datetime.now()
    print("Login Time: ", now.strftime("%Y-%m-%d_%H:%M:%S"))

enter_name("tim")

@calculate_time
def print_name(): 
    print("This is my")
    time.sleep(5)

#print_name()

