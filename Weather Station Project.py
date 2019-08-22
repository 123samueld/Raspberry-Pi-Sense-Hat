from sense_hat import SenseHat
sense = SenseHat()
from time import sleep


y = (255, 255, 0)
b = (0,0,0)
r = (255,0,0)
bl = (0,0,255)
g = (0,255,0)

smiley_face=[y,y,y,y,y,y,y,y,
             y,y,y,y,y,y,y,y,
             y,b,b,y,y,b,b,y,
             y,b,b,y,y,b,b,y,
             y,y,y,y,y,y,y,y,
             y,b,b,y,y,b,b,y,
             y,y,y,b,b,y,y,y,
             y,y,y,y,y,y,y,y]

cold_frowning_face=[bl,bl,bl,bl,bl,bl,bl,bl,
                    bl,bl,bl,bl,bl,bl,bl,bl,
                    bl,b,b,bl,bl,b,b,bl,
                    bl,b,b,bl,bl,b,b,bl,
                    bl,bl,bl,bl,bl,bl,bl,bl,
                    bl,bl,bl,b,b,bl,bl,bl,
                    bl,bl,b,bl,bl,b,bl,bl,
                    bl,b,bl,bl,bl,bl,b,bl]

hot_frowning_face=[ bl,bl,bl,bl,bl,bl,bl,bl,
                    bl,bl,bl,bl,bl,bl,bl,bl,
                    bl,r,r,bl,bl,r,r,bl,
                    bl,r,r,bl,bl,r,r,bl,
                    bl,bl,bl,bl,bl,bl,bl,bl,
                    bl,bl,bl,r,r,bl,bl,bl,
                    bl,bl,r,bl,bl,r,bl,bl,
                    bl,r,bl,bl,bl,bl,r,bl]



def temp():
    measures=int(input("Enter number of measurements to be taken: \n"))
    temp=[]
    for i in range(0,measures):
        meas=sense.get_temperature()
        temp.append(meas)
    avg=sum(temp)/measures
    average=round(avg,2)
    print("Average of measurements is: ",average,"\n")
    sense.show_message(str(average))
    if average >20:
        sense.show_message("Hot")
        sense.set_pixels(hot_frowning_face)
        sleep(3)
        sense.clear()
    elif average >= 15  <= 20:
        sense.show_message("Perfect")
        sense.set_pixels(smiley_face)
        sleep(3)
        sense.clear()
    elif average < 15:
        sense.show_message("Cold")
        sense.set_pixels(cold_frowning_face)
        sleep(3)
        sense.clear()
    menu()
    
def temp_saver():
    measures=int(input("Enter number of measurements to be taken: \n"))
    temp=[]
    for i in range(0,measures):
        meas=sense.get_temperature()
        temp.append(meas)
    avg=sum(temp)/measures
    average=round(avg,2)
    print("\n *** Average temp is: ",average," *** \n")
    f=open("Temperature Report.txt", "w")
    f.write(str(temp))
    f.write(str(average))
    f.close()
    print("\n *** Temperature report has been saved *** ")
    menu()



def humidity():
    measures=int(input("Enter number of measurements to be taken: \n"))
    hum=[]
    for i in range(0,measures):
        meas=sense.get_humidity()
        hum.append(meas)
    avg=sum(hum)/measures
    average=round(avg,2)
    print("\n *** Average humidity is: ",average," *** \n")
    sense.set_pixels(cold_frowning_face)
    sleep(3)
    sense.clear()
    menu()
def pressure():
    measures=int(input("Enter number of measurements to be taken: \n"))
    press=[]
    for i in range(0,measures):
        meas=sense.get_pressure()
        press.append(meas)
    avg=sum(press)/measures
    average=round(avg,2)
    print("\n *** Average pressure is: ",average," *** \n ")
    sense.set_pixels(hot_frowning_face)
    sleep(3)
    sense.clear()
    menu()

def end():
    print("\n *** Ending the program ***")
    
def menu():
    option =input("Please choose an option: \n 1) Find the Temperature  \n 2) Save the temperature \n 3) Find the humidity \n 4) Find the pressure \n 5) End the program \n(1/2/3/4/5)\n")
    sense.show_message("Options: 1 temp, 2 save, 3 humid, 4 pressure, 5 end.")
    if option == "1":
        temp()
    elif option == "2":
        temp_saver()
    elif option == "3":
        humidity()
    elif option == "4":
        pressure()
    elif option == "5":
        end()
    else:
        print("\n *** Sorry that's not an option \n *** ")
        menu()
menu()

