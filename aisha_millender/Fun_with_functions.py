#create a loop that counts from 1 to 2000 that prints the number of that iteration and specifiy even or odd
def odd_even():
    for num in range(0, 2001):
        if num % 2 == 0:
            print "My number is ", str(num) + ".", "This is an even number."
        else:
            print "My number is ", str(num) + ".", "This is an odd number."

odd_even()