#nested dictionary
Quiz = {    
    1 : {
        'que' : 'Who is pm of india ',
        'ans' : 'narendra modi',
    },
    2 : {
        'que' : 'most popular programming language',
        'ans' : 'java',

    }
}

size= len(Quiz)
#print(size)

for k in range(1, size+1):
    print("que: ",Quiz[k]['que'])
    ans= input("Enter your ans")
    if Quiz[k]['ans'] == ans:
        print("right answer")
    else: 
        print("flase answer")    
