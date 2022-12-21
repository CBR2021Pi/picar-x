from picarx import Picarx
import time

angle = 0
servoSetTime = 0.01


def main():   
    global angle 
    try:
        px = Picarx()
        px.set_dir_servo_angle(angle)
        # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
        px.forward(0)
        while True:
            distance1 = px.ultrasonic.read()
            time.sleep(0.1)
            distance2 = px.ultrasonic.read()
            time.sleep(0.1)
            distance3 = px.ultrasonic.read()
            
            distance = (distance1 + distance2 + distance3) / 3
            
            print("distance: {:0.2f}  angle: {}".format(distance, angle))
            
            if distance > 0:
                if distance < 25:
                    #px.set_dir_servo_angle(-35)
                    while angle > -35:
                        angle -= 2
                        print("angle: {}".format(angle))
                        px.set_dir_servo_angle(angle)
                        time.sleep(servoSetTime)
                        
                    
                    #for angle in range(0,-35,-1):
                    #    print("angle: {}".format(angle))
                    #    px.set_dir_servo_angle(angle)
                    #    time.sleep(servoSetTime)
                    
                else:
                     while angle < 0:
                        angle += 2
                        print("angle: {}".format(angle))
                        px.set_dir_servo_angle(angle)
                        time.sleep(servoSetTime)
                        
                    #px.set_dir_servo_angle(0)
                    #for angle in range(-35,1):
                    #    print("angle: {}".format(angle))
                    #    px.set_dir_servo_angle(angle)
                    #    time.sleep(servoSetTime)
            
    finally:
        px.forward(0)


if __name__ == "__main__":
    main()

