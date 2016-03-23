"""

 ** Ask the user for a file name. This text file should contain a sequence of integers, one per line.
    e.g.
    1
    2
    5
    7
    9
 ** Read in this data and store it in an array (or list, if the language doesn't have pure arrays).
 ** Find the percentage of odd numbers in the array and display that to the user.

    The program must include a function that is passed the array (or list) and returns the count of the odd numbers in that list.
    You should use that function in your program.

    Please comment your code based on the style you learned in your previous studies.

"""

import sys
import os.path

#
# Test file exists from user input
#
def load_file():

   while True:
       input = raw_input('Enter a file name >> ')
       if input and not input.isspace():
           if os.path.isfile(input):
              return input
           else:
              again = raw_input('Would you like to try again ? Y or N >>')
              if (again != 'Y' and again != 'y'):
                  break

#
# Load file into list or dictionary
# Non integers will not load into list
# Removing spaces and newline characters
#
def load_ints(pFile):

   integers_list = []

   if pFile:
       integers_file = open(pFile, 'r');
       for line in integers_file.readlines():
          line_value = line.rstrip('\n').strip()
          if is_integer(line_value):
              integers_list.append(line_value)
       integers_file.close()
       return integers_list

#
# Count number of ints, percentage of odds in the list
#
def count_odd_ints(pList):

   odd_ducks = 0

   if type(pList) is list:

       for i in pList:

           if even_or_odd(i) == "Odd":
               odd_ducks += 1

       return odd_ducks

#
# Evaluate integer as even or odd
# Using modulus, when dividing by 2 should be zero for even - no remainder
# Also note that only integers can be odd or even
#
def even_or_odd(pVal):

   if pVal:
       if int(float(pVal)) % 2 == 0:
           return "Even"
       else:
           return "Odd"

def is_integer(pVal):

    try:
        if float(pVal) % 1 == 0 or float(pVal) % 2 == 0:
            return True
        else:
            # @ this point, this is not an integer - most likely a decimal
            return False

    except ValueError:
        # @ this point, this is not an integer - most likely non-numeric
        return False

if __name__ == "__main__":

   file_name = load_file()
   ints_list = load_ints(file_name)
   nmbr_odds = count_odd_ints(ints_list)

   # assume if odds returned that file was loaded
   # keep an eye out for division by zero, list might not contain any integers
   if nmbr_odds != None:
       if len(ints_list) > 0:
           percent_odd = (float(nmbr_odds) / float(len(ints_list))) * 100
           print 'there are {0} odd integers in the file "{1}". With {2} total integers, that is a {3:.2f}% of odd integers.'.format(nmbr_odds, file_name, len(ints_list), percent_odd)
       else:
           print 'There were not any integers in your file'
