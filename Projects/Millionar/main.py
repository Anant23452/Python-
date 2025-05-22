qustions =[ ["Who is sharukh khan","Actor","worker","gym trainer","Plumber",1],
    ["What is india","state","village","contary","planet",3],
    ["Who is amir khan","Actor","worker","gym trainer","Plumber",1],
    ["Who is salman khan","Actor","worker","gym trainer","Plumber",1]
    ]

for qustion in qustions:
    print(qustion[0])
    print(f"a.{qustion[1]}")
    print(f"b.{qustion[2]}")
    print(f"c.{qustion[3]}")
    print(f"c.{qustion[4]}")

#check whether the answer is correct or not
    a = int(input("Enter your answer 1 for a,2 for b, 3 for c , 4 fro d::"))
    if(qustion[5]==a):
        print("correct Answer")
    else:
        print(f"Incorrect,the correct answer was{qustion[5]}")
        print("Better luck next time")