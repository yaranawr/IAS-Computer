from helpers import hex_to_bin, bin_to_hex, check_word

class IAS:
    def __init__(self):
        self.memory = [0] * 1000
        self.ac = 0
        self.pc = 0

    def load(self, address):
        self.ac = self.memory[int(address, 2)]

    def store(self, address):
        self.memory[int(address, 2)] = self.ac 

    def jump(self, address):
        self.pc = int(address, 2) 

    def add(self, address):
        self.ac += self.memory[int(address, 2)] 

    def sub(self, address):
        self.ac -= self.memory[int(address, 2)]  

    def read_instruction(self, instruction):
        bin_instruction = hex_to_bin(instruction)

        valid, error_message = check_word(bin_instruction)
        if not valid:
            print(error_message)
            return
        
        left_opcode = bin_instruction[:8]      
        left_address = bin_instruction[8:20]    
        right_opcode = bin_instruction[20:28]   
        right_address = bin_instruction[28:40] 


        self.get_IAS_instruction(left_opcode, left_address)
        if right_opcode != "00000000":
            self.get_IAS_instruction(right_opcode, right_address)

    def get_IAS_instruction(self, opcode, address):
        match opcode: 
            case "00000001":
                self.load(address)
            case "00100001":
                self.store(address)
            case "00001101":  # Left jump
                self.jump(address)
            case "00001110":  # right jump
                self.jump(address)
            case "00000101":
                self.add(address)
            case "00000110":
                self.sub(address)
            case _:
                print(f"Unknown opcode: {opcode}")

    def run(self):
        while self.pc < len(self.memory):
            word = self.memory[self.pc]
            if word == 0:  
                print(f"Sum result = {computer.memory[102]}")
                break

            self.read_instruction(word)
            self.pc += 1


computer = IAS()

computer.memory[100] = 1
computer.memory[101] = 2

instruction_1 = "0000000100000110010000000101000001100101"
instruction_2 = "0010000100000110011000000000000000000000"

computer.memory[0] = bin_to_hex(instruction_1)
computer.memory[1] = bin_to_hex(instruction_2) 

computer.run()

