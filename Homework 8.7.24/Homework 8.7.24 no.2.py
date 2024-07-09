#Start

score: int = int (input ("What's your test's score?"));
if score>=0 and score<=40:
    print ("Try harder next time...");
elif score>=41 and score<=60:
    print ("You're getting there, need some more work");
elif score>=61 and score<=80:
    print ("Pretty good");
elif score>=81 and score<=95:
    print ("Awesome!");
elif score>=96 and score<=100:
    print ("Excellent!!! You're a Star!");
else:
    print ("Illegal Grade");

#End