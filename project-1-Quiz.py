q1="""who is the best batminton player?
a)PV Sindhu
b)Saina Nehwal
c)Malvika Bansod
d)Aakarshi Kashyap"""

q2="""Who is the first educational minister in INDIA ?
a)Humayun Kabir
b)Siddharta Shankar Ray
c)Maulana Abul Kalam Azad
d)A.P.J.Abdul Kalam"""

q3="""Imagine you are in a sinking rowboat surrounded by sharks. How would you survive?
a)Killing the shark
b)Pouring the water into ocean
c)Befriending the shark
d)Stop imagining"""

q4="""Which type of Programming does Python support?
a)Object-oriented
b)Structured
c)Functional
d)All of the above"""

q5="""Who is the best dancer in tollywood?
a)Allu Arjun
b)N.T.R
c)Chiranjeevi
d)Ram Charan"""
question={q1:"a",q2:'c',q3:'d',q4:'b'}
name=input("Hi what is your name")
print("Hello",name,"Welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to ski this que(yes/no)")
    if flag1=="yes":
        continue
    ans=input("Enter your answer")
    if ans==questions[i]:
        print("Wow!You got one point")
        score=score+1
        print("Your current score is :",score)
    else:
        print("Wrong answer,u lost 1 mark")
        score=-1
        print("Your current score is :",score)
    flag2=input("Do you want to quit?(yes/no)")
    if flag2=="yes":
        break
    print("Your total score:",score)
