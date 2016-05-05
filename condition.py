def main():
    name = input("Please enter your name?")
    age= input("Please enter your age")
    print("Your name is {0} and your are {1} years old".format(name,age))

main()

def chapter1():
    print("Once upon a time there was a great guy named Jack Sharpe")

def chapter2():
    print("Jack had great jokes")

def main():
        chapter1()
        chapter2()

main()

def fn_sum(number1,number2): # parameters allow data to be passed into the function
    sum_number = number1 + number2
    return sum_number # the result needs to be returned so it is accessible to other functions

def main():
    user_num1 = int(input("Please enter a number "))
    user_num2 = int(input("Please enter another number "))
    answer = fn_sum(user_num1,user_num2) #calls s function and passes attributes to the parameters
    print("The sum is {0}".format(answer))
main()

def my_list():
    days = ["Milk","Eggs","Water","Flour","Sugar"]
    print(days)#print all items in the list
my_list();

#Add an item to the end of the list:
def my_list():
    days = ["Milk","Eggs","Water","Flour","Sugar"]
    days.append("AND SOME KFC")
    print(days)
my_list();
