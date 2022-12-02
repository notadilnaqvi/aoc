with open('01-input.txt') as f:
    content = f.read()
    elves = content.split('\n\n')
    calories_per_elf = []
    for elf in elves:
      calories = elf.split('\n')
      calories_of_current_elf = 0
      for calorie in calories:
        calories_of_current_elf += int(calorie)
      calories_per_elf.append(calories_of_current_elf)

    calories_per_elf_sorted = sorted(calories_per_elf, reverse=True)
    print(calories_per_elf_sorted[0] + calories_per_elf_sorted[1] + calories_per_elf_sorted[2])