p1 = "Make a lot off money"
p2 = "Buy now"
p3 = "Subscibe this"
p4 = "click this"

message = input("Enter your Comment")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("you are scammer")
else:
    print("You are not scammer")
    