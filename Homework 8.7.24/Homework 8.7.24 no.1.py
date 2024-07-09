#Start

print ("                                                ***1st Person***");
id1: str = str (input ("Please enter your ID number"));
fname1: str = str (input ("What's your First Name?"));
lname1: str = str (input ("And your Last Name?"));
height1: float = float (input ("How tall are you?"));
YoB1: int = int (input ("In Which year were you born?"));

print ("                                                ***2nd Person***");
id2: str = str (input ("Please enter your ID number"));
fname2: str = str (input ("What's your First Name?"));
lname2: str = str (input ("And your Last Name?"));
height2: float = float (input ("How tall are you?"));
YoB2: int = int (input ("In Which year were you born?"));

print ("                                                ***3rd Person***");
id3: str = str (input ("Please enter your ID number"));
fname3: str = str (input ("What's your First Name?"));
lname3: str = str (input ("And your Last Name?"));
height3: float = float (input ("How tall are you?"));
YoB3: int = int (input ("In Which year were you born?"));

print (f"#ID:{id1} Name: {lname1}, {fname1:<10} Height: {height1:<10.2f} Year of Birth: {YoB1}")
print (f"#ID:{id2} Name: {lname2}, {fname2:<10} Height: {height2:<10.2f} Year of Birth: {YoB2}")
print (f"#ID:{id3} Name: {lname3}, {fname3:<10} Height: {height3:<10.2f} Year of Birth: {YoB3}")

#End
