def main():
    calories = []
    with open('input.txt', 'r') as file:
        cur = 0

        for line in file:
            if line == '\n':
                calories.append(cur)
                cur = 0
            else:
                idk = line.strip()
                cur = cur + int(idk)

    three = []
    for i in range(0,3):

        three.append(max(calories))
        calories.remove(max(calories))

    return sum(three)

print(main())
