input_number = float(input("Please enter a number: "))

if (input_number % 3 == 0) and (input_number % 5 == 0):
    print("fizzbuzz")

else:
    if (input_number % 3 == 0):
      print("fizz")

   if (input_number % 5 == 0):
      print("buzz")