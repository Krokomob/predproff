class studentiki:
    fio=''
    score=0

f=open('students.csv')
students=[]

j=0
for i in f:
    s = i.split(',')
    if s[3][:-1]=='10':
        students.append(studentiki())
        students[j].fio=s[1]
        students[j].score = int(s[4])
        j+=1

for i in range(len(students)):
    j=i
    t=students[i]
    while j>0 and students[j-1].score<t.score:
        students[j]=students[j-1]
        j-=1
    students[j]=t


s = students[0].fio.split()

print('1 место: '+s[1][:1]+'.'+s[0])
s = students[1].fio.split()
print('2 место: '+s[1][:1]+'.'+s[0])
s = students[2].fio.split()
print('3 место: '+s[1][:1]+'.'+s[0])

