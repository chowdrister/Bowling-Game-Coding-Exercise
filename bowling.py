# Bowling Calculator Project

fullScore = input('Enter bowling score: ')

Frames = fullScore.split('-') #parse through input string to remove the hyphens

#Initialize a global int "totalScore" and array "Throws" that we can add to as the script runs
totalScore = 0
Throws = []

#iterate through each frame to create an array of individual throws
for index in range(len(Frames)):
    if Frames[index][0] == 'X' and len(Frames[index]) == 1:
        Throws.append('X')
    elif Frames[index][0] == 'X' and len(Frames[index]) == 3:
        Throws.extend([Frames[index][0], Frames[index][1], Frames[index][2]])
    elif Frames[index].endswith('/'):
        Throws.extend([int(Frames[index][0]), 10 - int(Frames[index][0])])
    elif len(Frames[index]) == 1:
        Throws.extend([int(Frames[index][0])])
    else:
        Throws.extend([int(Frames[index][0]), int(Frames[index][1])])
   
#iterate through the "Throws" array and assign values to all strikes, leftover spares, and characters that haven't been cast to string (mostly last frame edge cases)
for index in range(len(Throws)):
    if Throws[index] == 'X':
        Throws[index] = 10
    elif Throws[index] == '/':
        Throws[index] = 10 - int(Throws[index - 1])
    else:
        Throws[index] = int(Throws[index])
        

#initialize position and counterbalance variable
position = 0
counterbalance = 1

#check to see if final frame has a strike or a spare in order to adjust counterbalance
if 'X' in Frames[9] or '/' in Frames[9]:
    counterbalance = 2

#add to totalScore based on throws
while position < (len(Throws) - counterbalance):
    if Throws[position] == 10:
        totalScore += 10 + Throws[position + 1] + Throws[position + 2]
        position += 1
    elif Throws[position] + Throws[position + 1] == 10:
        totalScore += 10 + Throws[position + 2]
        position += 2
    else:
        totalScore += Throws[position] + Throws[position + 1]
        position += 2

print('Total score is', totalScore)
    
    