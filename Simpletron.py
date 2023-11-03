class Simpletron:
    def __init__(self):
        self.memory = [0] * 100  # Initialize memory with 100 locations
        self.accumulator = 0  # Accumulator for arithmetic operations
        self.instruction_counter = 0  # Instruction counter to keep track of the current instruction

    def read_instruction(self):
        print("*** Welcome to Simpletron! ***")
        print("*** Enter your program one instruction at a time. ***")
        print("*** Each instruction must be a positive or negative number, or -99999 to halt. ***")

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

    def execute_program(self):
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
                break
            self.instruction_counter += 1


def main():
    s = Simpletron()
    s.read_instruction()
    s.instruction_counter = 0
    s.execute_program()


if __name__ == "__main__":
    main()
