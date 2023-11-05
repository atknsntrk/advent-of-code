def handle():
    with open('input.txt', 'r') as file:
        score = 0
        for line in file:
            a, b = line.split(" ")
            b = b.strip()





            if a == "A" and b.strip() == "X":
                print("Do we enter?")
                score = score + 3
            elif a == "A" and b == "Y":
                score = score + 4
            elif a == "A" and b == "Z":
                score = score + 8
            elif a == "B" and b == "X":
                score = score + 1
            elif a == "B" and b == "Y":
                score = score + 5
            elif a == "B" and b == "Z":
                score = score + 9
            elif a == "C" and b == "X":
                score = score + 2
            elif a == "C" and b == "Y":
                score = score + 6
            elif a == "C" and b == "Z":
                score = score +7
    return score

print(handle())


