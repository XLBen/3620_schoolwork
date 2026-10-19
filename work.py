import csv


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
    return age,hg,cls 
load_data("stroke_separable.csv")
    
