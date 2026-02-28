# FILE NAME - convert_C_to_F_02.py

# NAME: Robert Young
# DATE: 02/28/2026
# BRIEF DESCRIPTION: Create module that asks a user to convert temp from C to F or F to C. Then asks for the Temp.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
def main():
    def convert_temp():
        # c to f = temperature * 9/5 + 32
        # f to c = (temperature - 32 ) * 5/9
      print("===== Temperature Converter =====") 
      print()
      print(" 1. Convert from Celsius to Fahrenheit")
      print(" 2. Convert from Fahrenheit to Celsius")
      print()
      choice = int(input("Please choose from the above menu: "))
      temperature = int(input("Enter a temperature to convert: "))
      if choice == 1:
         convert_temp = temperature * 9/5 + 32
         print(f"{temperature} degrees Celsius is {convert_temp} degrees Fahrenheit.")
      elif choice == 2:
        convert_temp = (temperature - 32) * 5/9
        print(f"{temperature} degrees Fahrenheit is {convert_temp} degrees Celsius.")
    convert_temp()
main()

########### END YER CODE ABOVE THIS LINE ###########

########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

I didn't really learn anything new, just getting into the flow of writing code and inmporting previous modules. 


'''
