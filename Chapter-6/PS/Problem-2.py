sub1 = int(input("Enter First subject Marks: "))
sub2 = int(input("Enter Second subject Marks: "))
sub3 = int(input("Enter Third subject Marks: "))

persentage = (sub1 + sub2 + sub3)/3

print("Your Persentage is :",persentage)

if(sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and persentage >= 40):
    print("You are pass")
else:
    print("you are fail")