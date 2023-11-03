class Simpletron:
    def __init__(self):
        self.memory = [0] * 100  # Initialize memory with 100 locations
        self.accumulator = 0  # Accumulator for arithmetic operations
        self.instruction_counter = 0  # Instruction counter to keep track of the current instruction

    def read_instruction_from_file(self):
        filename = input("Enter the name of the input text file: ")
        try:
            with open(filename, 'r') as file:
                for line in file:
                    instruction = int(line.strip())
                    if instruction == -99999:
                        break
                    self.memory[self.instruction_counter] = instruction
                    self.instruction_counter += 1
            print("Instructions loaded successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except ValueError:
            print("Invalid instruction in the file. Please provide valid integers.")

    def read_instruction(self):
        while True:
            try:
                instruction = int(input(f"{self.instruction_counter:02d} ? "))

                if instruction == -99999:
                    break

                # Store the instruction in memory
                self.memory[self.instruction_counter] = instruction
                self.instruction_counter += 1
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def dump_memory(self):
        print("\nMemory Dump:")
        for i in range(0, 100, 10):
            for j in range(i, i + 10):
                print(f"{self.memory[j]:+05d}", end=" ")
            print()

    def execute_program(self):
        print("*** Program loading completed ***")
        print("*** Program execution begins ***")
        while self.instruction_counter < len(self.memory):
            opcode = self.memory[self.instruction_counter] // 100
            operand = self.memory[self.instruction_counter] % 100

            if opcode == 10:  # READ
                value = int(input("Please enter a value: "))  # Read the value from the user
                self.memory[operand] = value
            elif opcode == 11:  # WRITE
                print(self.memory[operand])
            elif opcode == 20:  # LOAD
                self.accumulator = self.memory[operand]
            elif opcode == 21:  # STORE
                self.memory[operand] = self.accumulator
            elif opcode == 30:  # ADD
                self.accumulator += self.memory[operand]
            elif opcode == 31:
                self.accumulator -= self.memory[operand]
            elif opcode == 32:
                self.accumulator //= self.memory[operand]
            elif opcode == 33:
                self.accumulator *= self.memory[operand]
            elif opcode == 40:
                self.instruction_counter = operand
            elif opcode == 41:
                if self.accumulator < 0:
                    self.instruction_counter = operand
                    continue
            elif opcode == 42:
                if self.accumulator == 0:
                    self.instruction_counter = operand
                    continue
            elif opcode == 43:
                print("*** Simpletron execution terminated ***")
                self.dump_memory()
                break

            self.instruction_counter += 1


def main():
    s = Simpletron()
    print("*** Welcome to Simpletron! ***")
    print("*** Please enter your program one instruction ***")
    print("*** ( or data word ) at a time into the input ***")
    print("*** text field. I will display the location ***")
    print("*** number and a question mark (?). You then ***")
    print("*** type the word for that location. Enter ***")
    print("*** -99999 to stop entering your program. ***")
    print("")
    choice = input("Enter '1' to read instructions from a file, or '2' to input instructions interactively: ")

    if choice == '1':
        s.read_instruction_from_file()
    elif choice == '2':
        s.read_instruction()
    else:
        print("Invalid choice. Please enter '1' or '2'.")
    s.instruction_counter = 0
    s.execute_program()


if __name__ == "__main__":
    main()
