import time


def is_amstrong_number(number):

    digits_of_number = [int(x) for x in str(number)]

    total = 0 

    number_of_digits = len(digits_of_number)

    i = 0

    while ( i < number_of_digits ):

        total = total + ( digits_of_number[i] ** number_of_digits )

        i = i + 1
        

    if ( total == number ) :
        return True

    else:
        return False



def next_or_previous_amstrong_number(number,next_or_previous):  # next_or_previous = True for next and False for previous
    
     current_number = number

     i = 0 

     while (True):

         i = i + 1

         if (i > 100000):
             print ('Iteration limit exceeded')
             return 0

         if (next_or_previous == True) :
             current_number = current_number + 1

         else:
             current_number = current_number - 1
         
         check_amstrong_of_current_number = is_amstrong_number(current_number)

         if (check_amstrong_of_current_number == True):
             return current_number


def main_function(number):

    time_beginning = time.time()

    if (number < 1):
        print('Only natural Numbers as input')
        return True

    checK_if_number_is_amstrong = is_amstrong_number(number)

    if (checK_if_number_is_amstrong == True):
        print('given number ' + str(number)  + ' is amstrong')
    else: 
        print('Given number '  + str(number) + ' is not amstrong')

        previous_amstrong_number = next_or_previous_amstrong_number( number , 0 )
        print (' previous amstrong number is ' + str(previous_amstrong_number) )

        next_amstrong_number = next_or_previous_amstrong_number( number , 1 )
        print (' Next amstrong number is ' + str(next_amstrong_number) )

    time_end = time.time()
    
    time_of_execution = time_end - time_beginning

    print ('Time taken to execution the script was ' + str(time_of_execution) )

    return True



main_function(8208)

main_function(15000)