def main():
    location_1, location_2 = read_file()
    distance = calculate_distance(location_1, location_2)
    score = similarity_score(location_1, location_2)
    print(f"Distance is {distance}")
    print(f"Score is {score}")


def read_file():
    location_1 = []
    location_2 = []
    with open("day1.txt", "r") as file:
        for line in file:
            line = line.rstrip()
            location_1.append(int(line.split("   ")[0]))
            location_2.append(int(line.split("   ")[1]))
    location_1.sort()
    location_2.sort()
    return location_1, location_2


def calculate_distance(l1, l2):
    distance = 0
    for i in range(len(l1)):
        distance += abs(l1[i] - l2[i])
    return distance


def similarity_score(l1, l2):
    score = 0
    for i in range(len(l1)):
        score += l1[i] * l2.count(l1[i])
        print(score)
    return score


if __name__ == "__main__":
    main()
