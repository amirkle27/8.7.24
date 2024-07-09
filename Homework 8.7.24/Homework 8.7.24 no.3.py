#Start

vol: int = int(input ("Please enter the volume level from 0 to 10"));
match vol:
    case 0: print ("Mute");
    case 1: print ("Very Very Quiet");
    case 2: print ("Very Quiet");
    case 3: print ("Quiet");
    case 4: print ("Moderately Quiet");
    case 5: print ("Medium");
    case 6: print ("Moderately Loud");
    case 7: print ("Loud");
    case 8: print ("Very Loud");
    case 9: print ("Extremely Loud");
    case 10: print ("Too Loud!");

#End