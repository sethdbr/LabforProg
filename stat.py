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

fhand = open ('StudentExercise.csv')
next(fhand)
print(findhrs(fhand))
