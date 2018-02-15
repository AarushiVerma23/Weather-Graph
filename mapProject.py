import pygame
pygame.init()
w = pygame.display.set_mode([700,700])
w.fill((255,255,255))
b = (0,0,0)

data = []
month = []
day = []
x1 = 20
y1 = 650
x2 = 680
y2 = 650
x3 = 20
y3 = 650
x4 = 20
y4 = 50
days_month = 30.42
date = []

point = int(input("Enter a weather point in Celsius or type quit to exit: "))
data.append(point)
time1 = int(input("What month did this point occur at or type quit to exit? "))
time2 = int(input("What day did this point occur at or type quit to exit? "))
day = (time1,time2)
date.append(day)
print(date)

distancex = int((x2-x1)/12)
distancey = int((y3-y4)/12)

pointx = int((distancex*(int(time1) - 1)) + x1 + (distancex/days_month)*int(time2))
pointy = int(y3 - ((point/4)*50))

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
    

    pygame.draw.line(w,b,(x1,y1),(x2,y2))
    pygame.draw.line(w,b,(x3,y3),(x4,y4))
        

    x1 += distancex
    y3 -= distancey
    pygame.draw.line(w,b,(x1,y1 - 10),(x1,y1 + 10))
    pygame.draw.line(w,b,(x3 - 10,y3),(x3 + 10,y3))

    pygame.draw.circle(w,b,(pointx,pointy),1)
        
        
    pygame.display.flip()

    

    

    

    

    
