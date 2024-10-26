# C-ins translation
c_comp = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "M": "1110000",
    "!D": "0001101",
    "!A": "0110001",
    "!M": "1110001",
    "-D": "0001111",
    "-A": "0110011",
    "-M": "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101",
}

c_dest = {
    "" : "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111",
}

c_jump = {
    "" : "000",
    "JGT" : "001",
    "JEQ" : "010",
    "JGE" : "011",
    "JLT" : "100",
    "JNE" : "101",
    "JLE" : "110",
    "JMP" : "111",
}

a_predef = {
    "R0" : "0",
    "R1" : "1",
    "R2" : "2",
    "R3" : "3",
    "R4" : "4",
    "R5" : "5",
    "R6" : "6",
    "R7" : "7",
    "R8" : "8",
    "R9" : "9",
    "R10" : "10",
    "R11" : "11",
    "R12" : "12",
    "R13" : "13",
    "R14" : "14",
    "R15" : "15",
    "SCREEN": "16384",
    "KBD": "24576",
    "SP": "0",
    "LCL": "1",
    "ARG": "2",
    "THIS": "3",
    "THAT": "4",
}

fileName = "Pong.asm"
outName = "Pong.hack"

a_lables = {}
a_vars = {}
var_addr = 16
# pass 1: find lables
with open(fileName, "r") as prg:
    count = 0
    for line in prg:
        l = line.strip()
        if l == "" or l[0:2] == "//":
            continue
        if l[0] == "(" and l[-1] == ")":
            label = l[1:-1]
            a_lables[label] = str(count)
        else:
            count += 1


# pass 2: replace labes
with open(fileName, "r") as prg:
    with open("prgL.asm", "w") as prgL: 
        for line in prg:
            line = line.strip()
            # ignore empty
            if line == "" or l[0:2] == "//" or line[0] == "(" and line[-1] == ")":
                continue
            # found @
            if line[0] == "@":
                # pre defined symbol
                if line[1:] in a_predef:
                    line = "@" + a_predef[line[1:]]
                # labels
                elif line[1:] in a_lables:
                    line = "@" + a_lables[line[1:]]
                # known var
                elif line[1:] in a_vars:
                    line = "@" + a_vars[line[1:]]
                # new var
                elif not line[1:].isdecimal():
                    a_vars[line[1:]] = str(var_addr)
                    var_addr += 1
                    line = "@" + a_vars[line[1:]]
            
            prgL.write(line + "\n")


with open("prgL.asm", "r") as asm:
    with open(outName, "w") as hack:
        for line in asm:
            line = line.strip()
            # ignore empty
            if line == "" or line[0:2] == "//":
                continue
            # A-ins
            # @value
            if line[0] == "@":
                addr = int(line[1:], 10)
                bin = f'{addr:015b}'
                hack.write("0" + bin + "\n")
            
            # C-ins
            # dest = comp ; jump
            else:
                semico = line.split(";")            
                jump = semico[1] if len(semico)>1 else "" 
                left = semico[0].split("=")
                dest = left[0] if len(left)>1 else ""
                comp = left[1] if len(left)>1 else left[0] 
                
                bin = "111" + c_comp[comp] + c_dest[dest] + c_jump[jump] 
                hack.write(bin + "\n")