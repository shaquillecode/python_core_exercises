"""Draw a star"""
import turtle

tut =  turtle.Pen()

tut.color('black','yellow')
tut.begin_fill()

CNT = 0

#Draw a star
for x in range(1,15):
    tut.forward(300)
    tut.left(225)
    CNT += 1
    print("Count is: " +  str(CNT))

    # Stop drawing after 8 loops
    # If CNT > 7 and CNT < 9
    if CNT > 7:
        print("The star pattern is complete")
        break
tut.end_fill()
print("A star is born")
