def load_data(filename):
    fh = open(filename)
    header = next(fh)
    data = list()
    for line in fh:
        words = list(line.split(','))
        area = int(words[1])
        price = float(words[2]) * 1000
        cost = area * price / 10000000
        info = (cost , words[0])
        data.append(info)
    return data

def display(records):
    target=float(input("Maximum cost:"))
    for record in records:
        if record[0] < target :
            print(round(record[0],2) , record[1])

plots=load_data("plots.csv")
plots = sorted(plots, reverse =  True)
display(plots)

