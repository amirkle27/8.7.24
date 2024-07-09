#Start

kids: int = int (input("How many friends came to Danny's party?"))+1;
pizza: int = int (input("How many slices of pizza has Danny's mom ordered for the party?"));
slices: int = pizza // kids;
leftover: float = (pizza % kids);
print (f"After Danny's mom ordered {pizza} slices of pizza for {kids} kids, each kid got {slices:.0f} slices, with {leftover} slices left in the box");

#End