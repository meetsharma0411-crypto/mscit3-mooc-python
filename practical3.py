std = []

sub = ["python", "maths", "dbms", "statistics", "computer"]

for i in range(2):
    rn = int(input("roll number: "))
    nm = input("name: ")

    mk = []

    for s in sub:
        m = int(input(s + " marks: "))
        mk.append(m)

    tot = sum(mk)
    per = tot / 5

    if per >= 80:
        gr = "A"
    elif per >= 70:
        gr = "B"
    elif per >= 60:
        gr = "C"
    elif per >= 50:
        gr = "D"
    else:
        gr = "F"

    st = {
        "roll": rn,
        "name": nm,
        "marks": mk,
        "total": tot,
        "percentage": per,
        "grade": gr
    }

    std.append(st)

print("\nstudent details")

for s in std:
    print(s)

totper = 0

for s in std:
    totper = totper + s["percentage"]

avg = totper / 10

print("\nclass average:", avg)

high = std[0]["percentage"]
low = std[0]["percentage"]

for s in std:
    if s["percentage"] > high:
        high = s["percentage"]

    if s["percentage"] < low:
        low = s["percentage"]

print("\nhighest scorer:")

for s in std:
    if s["percentage"] == high:
        print(s["name"])

print("\nlowest scorer:")

for s in std:
    if s["percentage"] == low:
        print(s["name"])

print("\nstudents above average:")

for s in std:
    if s["percentage"] > avg:
        print(s["name"])

print("\nfailed students:")

for s in std:
    fail = False

    for m in s["marks"]:
        if m < 33:
            fail = True

    if fail:
        print(s["name"])

gd = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "F": []
}

for s in std:
    gd[s["grade"]].append(s["name"])

print("\ngrade wise students:")

for gr in gd:
    print(gr, gd[gr])

names = []

for s in std:
    names.append(s["name"])

sortnames = sorted(names)

print("\nalphabetical order:")
print(sortnames)

high = std[0]["percentage"]
second = 0

for s in std:
    if s["percentage"] > high:
        second = high
        high = s["percentage"]

    elif s["percentage"] > second and s["percentage"] != high:
        second = s["percentage"]

print("\nsecond highest scorer:")

for s in std:
    if s["percentage"] == second:
        print(s["name"])

print("\nsubject average:")

for i in range(5):
    subtot = 0

    for s in std:
        subtot = subtot + s["marks"][i]

    subavg = subtot / 10

    print(sub[i], ":", subavg)

dup = []

for i in range(10):
    for j in range(i + 1, 10):
        if names[i] == names[j]:
            if names[i] not in dup:
                dup.append(names[i])

print("\nduplicate names:")
print(dup)
