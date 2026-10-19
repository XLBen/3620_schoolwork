import csv
import random

def load_data(filename):
    
    age = []
    hg = []
    cls = []
    with open(filename,"r") as f:
        csvreader = csv.reader(f)
        next(csvreader)
        for row in csvreader:
            
            age.append(int(row[0]))
            hg.append(int(row[1]))
            cls.append(int(row[2]))

    print(age)
    print(hg)
    print(cls)
    print(len(age), len(hg), len(cls))
    return age,hg,cls 

def perceptron(age, hg, cls):
    random.seed(114514)
    randomnumber4age = random.uniform(-1, 1)
    randomnumber4hg = random.uniform(-1, 1)
    w0 = random.uniform(-1, 1)
    updated = False
    while True:
        updatedhowmanytimes = 0;
        updated = False;
        for i in range(len(age)):
            score = w0 + randomnumber4age*age[i] + randomnumber4hg*hg[i];
            if cls[i] == 1 and score < 0:
                w0 = w0 + 1;
                randomnumber4hg = randomnumber4hg +hg[i];
                randomnumber4age = randomnumber4age + age[i];
                updated = True;
                updatedhowmanytimes += 1;
            elif cls[i] == 0 and score >= 0:
                w0 = w0 - 1;
                randomnumber4hg = randomnumber4hg - hg[i];
                randomnumber4age = randomnumber4age - age[i];
                updated = True;
                updatedhowmanytimes += 1;
            if updatedhowmanytimes == 0:
                break
            return w0, randomnumber4age, randomnumber4hg


age, hg, cls = load_data("stroke_separable.csv")
w0, w_age, w_hg = perceptron(age, hg, cls)
print(w0, w_age, w_hg)