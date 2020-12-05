prog = ["jio a, +18",
"inc a",
"tpl a",
"inc a",
"tpl a",
"tpl a",
"tpl a",
"inc a",
"tpl a",
"inc a",
"tpl a",
"inc a",
"inc a",
"tpl a",
"tpl a",
"tpl a",
"inc a",
"jmp +22",
"tpl a",
"inc a",
"tpl a",
"inc a",
"inc a",
"tpl a",
"inc a",
"tpl a",
"inc a",
"inc a",
"tpl a",
"tpl a",
"inc a",
"inc a",
"tpl a",
"inc a",
"inc a",
"tpl a",
"inc a",
"inc a",
"tpl a",
"jio a, +8",
"inc b",
"jie a, +4",
"tpl a",
"inc a",
"jmp +2",
"hlf a",
"jmp -7"]

line = ""
ptr = 0
instruction = ""
value = 0
reg = ""
regA = 1
regB = 0
offst = 0

while 1:
    line = prog[ptr]
    instruction = line[:line.index(" ")]

    if instruction == 'hlf':
        reg = line[line.index(" ")+1:line.index(" ")+2]
        if reg == 'a':
            regA /= 2
            ptr += 1
        elif reg == 'b':
            regB /= 2
            ptr += 1
    if instruction == 'tpl':
        reg = line[line.index(" ")+1:line.index(" ")+2]
        if reg == 'a':
            regA *= 3
            ptr += 1
        elif reg == 'b':
            regB *= 3
            ptr += 1
    if instruction == 'inc':
        reg = line[line.index(" ")+1:line.index(" ")+2]
        if reg == 'a':
            regA += 1
            ptr += 1
        elif reg == 'b':
            regB += 1
            ptr += 1
    if instruction == 'jmp':
        if line[line.index(" ")+1] == "+":
            offst = int(line[line.index("+")+1:])
        if line[line.index(" ")+1] == "-":
            offst = (-1)*int(line[line.index("-")+1:])
        ptr += offst
    if instruction == 'jie':
        reg = line[line.index(" ")+1:line.index(" ")+2]
        if (reg == 'a' and regA % 2 == 0) or (reg == 'b' and regB % 2 == 0):
            if line[line.index(",")+2] == "+":
                offst = int(line[line.index("+")+1:])
            if line[line.index(",")+2] == "-":
                offst = int((-1)*line[line.index("-")+1:])
            ptr += offst
        else:
            ptr += 1
    if instruction == 'jio':
        reg = line[line.index(" ")+1:line.index(" ")+2]
        if (reg == 'a' and regA == 1) or (reg == 'b' and regB == 1):
            if line[line.index(",")+2] == "+":
                offst = int(line[line.index("+")+1:])
            if line[line.index(",")+2] == "-":
                offst = int((-1)*line[line.index("-")+1:])
            ptr += offst
        else:
            ptr += 1


    print("offst =", offst)
    print("line =", line)
    print("instruction =", instruction)
    print("register =", reg)
    print(ptr)

    if ptr >= len(prog):
        break

print("a =", regA)
print("b =", regB)

