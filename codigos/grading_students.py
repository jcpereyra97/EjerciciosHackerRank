def gradingStudents(grades):
    res = []
    for i in range(0,len(grades)):
        if (grades[i] < 38):
            continue
        else:
            x = True
            cont = 0
            comp = grades[i] % 5
            while(x):
                if(comp >= 3):
                    res.append(grades[i)
                elif(cont < 3):
                    res.append(grades[i] + cont)
                    x = False
                else:
                    res.append(grades[i])
                    x = False
    return res
        
        

print(34 % 5)
#print(gradingStudents([4,73,67,38,33]))