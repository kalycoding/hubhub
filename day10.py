def execute_instructions(instructions: list[str]) -> int:
    x = 1
    cycle = 0
    signal_strengthts = []
    signal_search = [20, 60, 100, 140, 180, 220]
    
    for instruction in instructions:
        if instruction.startswith('addx'):
            v = instruction.split()[1]

            x+=int(v)

            cycle+=1

            if cycle in signal_search:
                signal_strengthts.append(cycle * (x - int(v)))

            cycle+=1

            if cycle in signal_search:
                signal_strengthts.append(cycle * (x - int(v)))

        elif instruction == "noop":
            cycle+=1
            if cycle in signal_search:
                signal_strengthts.append(cycle * x)
                
    return sum(signal_strengthts)


instructions = []
with open('instructions.txt', 'r') as f:
    for line in f:
        instructions.append(line.strip())


print(execute_instructions(instructions))