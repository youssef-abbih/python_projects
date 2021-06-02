from art import logo

operations = {
              "+":lambda a,b : a+b,
              "-":lambda a,b : a-b,
              "*":lambda a,b : a*b,
              "/":lambda a,b : a/b
            }
def calculation():
  print(logo)
  end_calculation = False
  a = float(input("Enter the first number "))
  while not end_calculation:
    operation = input("Enter '+', '-', '*' or '/' ")
    b = float(input("Enter the second number "))
    operation_function = operations[operation]
    answer = operation_function(a,b)
    print(f"{a} {operation} {b} = {answer}")
    choice = input(f"Do you want to continue with {operation_function(a,b)}: 'yes' or 'new' for fresh calculation or 'no' ro quit ")

    if choice == 'yes':
      a = answer
    elif choice == 'no':
      end_calculation = True
    elif choice == "new":
      calculation()
calculation()
