ind = int(input("Enter Score: "))
aus= int(input("Enter Score: "))
pak = int(input("Enter Score: "))

if aus>pak:
    if aus>ind:
        print("Aus Won the Match")
    else:
        print("Ind won the match")
else:
    if pak>ind:
        print("Pak Won the match")
    else:
        print("ind won the match")                
