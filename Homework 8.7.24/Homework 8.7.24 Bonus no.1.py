#Start

pizza: int = int (input("How many slices of pizza has Danny's mom ordered for the party?"));
slices: int = pizza // 4;
leftover: float = (pizza % 4);
print (f"After Danny's mom ordered {pizza} slices of pizza, each kid got {slices:.0f} slices, with {leftover} slices left in the box");

#End