n = int(input());
tmp = n;
y = 0;
a = [];
e = False;
while(n!=0):
    i = n % 10;
    a.append(i);
    n = n // 10;

#logic
for j in range(0, len(a)):
    for k in range(j+1, len(a)):
        if(a[j] == a[k]):
            print("The key is : ", a[k]);
            e = True;

if(e == False):
    print("-1");