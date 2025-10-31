import matplotlib.pyplot as plt

def findhrs(Exercisehrs):
    ls = []
    for line in Exercisehrs:
            hrs = line.split(',')
            hr = hrs[0]
            if hr == '':
                continue
            else:
                hr = float(hrs[0])
                ls.append(hr)
    return(ls)
def average(ListofExercise):
    return sum(ListofExercise)//len(ListofExercise)

def prop_above(LsExercise,avg1):
    i = 0
    for num in LsExercise:
        if num > avg1:
            i += 1
    return(i/len(LsExercise))*100

def median(SortedList):
    middle = int(len(SortedList)/2)
    middle1 = SortedList[middle]
    return middle1

def hist(data,n_bins):
    plt.hist(data,bins = n_bins)
    plt.title("Hours of Exercise")
    plt.ylabel("Counts")
    plt.show()

fhand = open ('StudentExercise.csv')
next(fhand)
hrs_list = findhrs(fhand)
avg = average(hrs_list)
print("the average is ~",avg,"hrs")
print(f"The prop above is {prop_above(hrs_list, avg):.1f}%")
print("the median is",median(hrs_list),"hrs")
hist(hrs_list,15)
