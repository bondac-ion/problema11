n=int(input('Dati numarul de elemente din vector='))
z=[]
# if n<10:
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    z.extend([x])
print(z)

print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
a=z
print(a[::5])
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
b=z
print(b[::-1])
print('c)  sortează componentele tabloului în ordine descrescătoare;')
c=sorted(z)
c.sort(reverse=True)
print(c)
print('d)  afişează pe ecran doar componentele pare;')
d=[]
for i in range(0,len(z)):
    if z[i]%2==0:
        y=z[i]
        d.extend([y])
print(d)
print('e)  afişează pe ecran media aritmetică a componentelor pare;')
e=[]
t=0
for i in range(0,len(z)):
    if z[i]%2==0:
        t+=1
        y=z[i]
        e.extend([y])
print(sum(e)/t)
print('f)  afişează pe ecran doar componentele impare;')
f=[]
for i in range(0,len(z)):
    if z[i]%2!=0:
        y=z[i]
        f.extend([y])
print(f)
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x=int(input("Dati un numar:"))
y=int(input("Dati un numar:"))
g=[]
for i in range(0,len(z)):
    if z[i]%y!=0 and z[i]>x:
        v=z[i]
        g.extend([v])
print(g)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
x=int(input("Dati un numar:"))
y=int(input("Dati un numar:"))
h=[]
for i in range(0,len(z)):
    if z[i]<y and z[i]>x:
        w=z[i]
        h.extend([w])
print(h)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
i=[]
for p in range(0,len(z)):
    if z[p]%2!=0 and z[p]<0:
        y=z.index(z[p])
        i.extend([y])
print(i)
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
j=[]
for i in range(0,len(z)):
    if (z[i]>9 and z[i]<100) or (z[i]>-100 and z[i]<-9):
        y=z.index(z[i])
        j.extend([y])
print(j)
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
k=z.copy()
k[0]=min(k)
print(k)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
l=z.copy()
l[l.index(min(l))]=l[0]
print(l)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
m=[]
for i in range(0,len(z)):
    if z[i]%2==0:
        y=z[i]
        m.extend([y])
print(m)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
n=[]
for i in range(0,len(z)):
    if z[i]%3==0:
        y=z[i]
        n.extend([y])
print(n)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori.')
o=[]

for i in range(0,len(z)):
    q=[]
    for j in range(0,z[i]):
        if z[i]%(j+1)==0:
            q.extend([j+1])
    for j in range(z[i]-1,-1):
        if z[i]%(j+1)==0:
            q.extend([j+1])
            q.extend([-j-1])
    if len(q)<=4:
        o.extend([z[i]])
print(o)