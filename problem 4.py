import math
sin=math.sin
cos=math.cos
tan=math.tan
fact=math.factorial
sqr=math.sqrt

while True:
    re=input('please enter +, -, *, /, sin, cos, tan, cot, fact, sqr, exit: ')
    if re=="exit"
    break
    a=int(input("enter a: "))
    
    if re=="+":
        b=float(input("enter b: "))
        R=a+b

    if re=="-":
        b=float(input("enter b: "))
        R=a-b

    if re=="*":
        b=float(input("enter b: "))
        R=a*b

    if re=="/":
        b=float(input("enter b: "))
        if b==0:
            R="you cant enter zero for b :<"
        else:
            R=a/b

    if re=="sin":
        R=(math.sin(math.radians(a)))

    if re=="cos":
        R=(math.cos(math.radians(a)))

    if re=="tan":
            R=(math.tan(math.radians(a)))

    if re=="cot":
            z=(math.tan(math.radians(a)))
            R=(1)/z

    if re=="fact":
        R=math.factorial(a)

    if re=="sqr":
        if a<0:
            "We can`t do this"
        else:
            R=math.sqrt(a)

    print(R)
