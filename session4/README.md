# Assignment: EPAi Session 3, Numeric Types

## 1. Objective : Write all the functions given in the assignment and Pass all the unit test scenarios.
       Functions
	   a) Write function which returns a string encoding in the "base" for the the "number" using the "digit_map" with multiple value error exceptions.
	   b) Write function float_equality_testing which emulates floating point equality similar to isclose()
       c) Write function manual_truncation_function which truncates decimal point without using int() or math.trunc()
       d) Write function manual_rounding_function which round without using system defined ROUND function
	   Unit testing based on PEP8 styling
         - PEP 8, 4 spaces for indentations
         - Naming convention for function and classes
	   Readme with proper documentation 

## 2. Documentation on Functions used.
   a) Fn encoded_from_base10
	 This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module
	
	#Digit_map : Digit_map is the mapping used for generating the final encoding in the target base.
				 For example : Digital map of Hex is 0123456789ABCDEF with base 16
							   Digital map of Binary is 01 with base 2.
				 Like wise we can create digital map 
				 -length of digit_map should be greater than or equal to base value 
				 -Digital map should not have repeating characters.
    
    # Encoding will convert the number from base 10 to base specified. 

   #math
	math library in python have in-built functions such as isclose(), trunc(), round()
	The following functions are replica of the these function, but used without using them
   
   b) float_equality_testing
     This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
	 #is.close()
     The math.isclose() method checks whether two values are close, or not. 
	 This method returns a Boolean value: True if the values are close, otherwise False
     math.isclose(a, b, rel_tol = value, abs_tol = value)
		 
      rel_tol() - This function calculates the relative tolerance of two float numbers compares with 1e-12.
	  abs_tol() - This function calculates the absolute tolerance of two float numbers compares with 1e-05.
	  For float_equality testing, compare with compare with abs_tol() if the numbers are too close or rel_tol() if the numbers are not too close.
	
   c) manual_truncation_function
      This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
      It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
      
	  #Trunc() 
		  The truncation function truncates the number and returns only the integer part.
		  
   d) manual_rounding_function
       This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
       expected to write your one manually.
	   
	   #Round()
			The round() function returns a floating point number that is a rounded version of the specified number, with the 
        specified number of decimals.
	   



#zero',
#away'	
#bin(',
#hex(',
	

