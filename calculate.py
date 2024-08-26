class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def menu(self):
        while True:
            print("1-Addition 2-Extraction 3-Division 4-Multiplication 5-Exit")
            choice = input("Please select an operation: ")

            if choice == '1':
                self.addition()
            elif choice == '2':
                self.extraction()
            elif choice == '3':
                self.division()
            elif choice == '4':
                self.multiplication()
            elif choice == '5':
                print("Exited successfully")
                break
            else:
                print("Please enter a valid number")

    def addition(self):
        result = self.number1 + self.number2
        print(f"Result: {result}")

    def extraction(self):
        result = self.number1 - self.number2
        print(f"Result: {result}")
    
    def division(self):
        if self.number2 != 0:
            result = self.number1 / self.number2
            print(f"Result: {result}")
        else:
            print("Error: Division by zero is not allowed")

    def multiplication(self):
        result = self.number1 * self.number2
        print(f"Result: {result}")

calc = Calculator(5, 10)
calc.menu()
