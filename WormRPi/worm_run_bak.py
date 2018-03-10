#from Servo import Servo
from time import sleep

#parameters
delay = 3
max_angle = 90
swing_steps = 20
scale = 100.0

servo_array = [
[78,-0.63,-0.65,-0.62,-0.58,-0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[219,-0.63,-0.65,-0.62,-0.58,-0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[375,-0.63,-0.65,-0.62,-0.58,-0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[531,0.63,0.00,-0.62,-0.58,-0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[672,0.63,0.65,-0.62,-0.58,-0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[812,0.63,0.65,0.00,-0.58,-0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[937,0.63,0.65,0.62,-0.58,-0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[1047,0.63,0.65,0.62,0.00,-0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[1156,0.63,0.65,0.62,0.58,-0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[1344,0.63,0.65,0.62,0.58,0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[1515,-0.63,0.65,0.62,0.58,0.55,0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[1672,-0.63,0.65,0.62,0.58,0.55,0.51,0.00,-0.44,-0.41,-0.37,-0.34,-0.30],
[1781,-0.63,0.00,0.62,0.58,0.55,0.51,0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[1906,-0.63,-0.65,0.62,0.58,0.55,0.51,0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[2031,-0.63,-0.65,0.62,0.58,0.55,0.51,0.48,0.44,-0.41,-0.37,-0.34,-0.30],
[2140,-0.63,-0.65,0.00,0.58,0.55,0.51,0.48,0.44,-0.41,-0.37,-0.34,-0.30],
[2265,-0.63,-0.65,-0.62,0.58,0.55,0.51,0.48,0.44,0.41,-0.37,-0.34,-0.30],
[2375,-0.63,-0.65,-0.62,0.58,0.55,0.51,0.48,0.44,0.41,0.37,-0.34,-0.30],
[2547,-0.63,-0.65,-0.62,-0.58,0.55,0.51,0.48,0.44,0.41,0.37,0.34,0.30],
[2656,-0.63,-0.65,-0.62,-0.58,0.55,0.51,0.48,0.44,0.41,0.37,0.34,0.30],
[2875,0.63,-0.65,-0.62,-0.58,-0.55,0.51,0.48,0.44,0.41,0.37,0.34,0.30],
[3000,0.63,-0.65,-0.62,-0.58,-0.55,0.51,0.48,0.44,0.41,0.37,0.34,0.30],
[3172,0.63,0.65,-0.62,-0.58,-0.55,-0.51,0.48,0.44,0.41,0.37,0.34,0.30],
[3297,0.63,0.65,0.00,-0.58,-0.55,-0.51,0.00,0.44,0.41,0.37,0.34,0.30],
[3406,0.63,0.65,0.62,-0.58,-0.55,-0.51,-0.48,0.44,0.41,0.37,0.34,0.30],
[3547,0.63,0.65,0.62,-0.58,-0.55,-0.51,-0.48,0.00,0.41,0.37,0.34,0.30],
[3765,0.63,0.65,0.62,0.58,-0.55,-0.51,-0.48,-0.44,-0.41,0.00,0.34,0.30],
[3875,0.63,0.65,0.62,0.58,0.00,-0.51,-0.48,-0.44,-0.41,-0.37,0.00,0.00],
[3984,0.00,0.65,0.62,0.58,0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,0.00],
[4109,-0.63,0.65,0.62,0.58,0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[4265,-0.63,0.00,0.62,0.58,0.55,0.00,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[4484,-0.63,-0.65,0.62,0.58,0.55,0.51,-0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[4687,-0.63,-0.65,-0.62,0.58,0.55,0.51,0.48,-0.44,-0.41,-0.37,-0.34,-0.30],
[4828,-0.63,-0.65,-0.62,0.58,0.55,0.51,0.48,0.44,-0.41,-0.37,-0.34,-0.30],
[4937,-0.63,-0.65,-0.62,0.00,0.55,0.51,0.48,0.44,0.41,-0.37,-0.34,-0.30],
[5047,-0.63,-0.65,-0.62,-0.58,0.55,0.51,0.48,0.44,0.41,0.37,-0.34,-0.30],
[5172,-0.63,-0.65,-0.62,-0.58,0.55,0.51,0.48,0.44,0.41,0.37,0.34,-0.30],
[5281,-0.63,-0.65,-0.62,-0.58,0.00,0.51,0.48,0.44,0.41,0.37,0.34,0.30],
[5390,0.00,-0.65,-0.62,-0.58,-0.55,0.51,0.48,0.44,0.41,0.37,0.34,0.30],
[5500,0.63,-0.65,-0.62,-0.58,-0.55,0.51,0.48,0.44,0.41,0.37,0.34,0.30],
[5625,0.63,0.00,-0.62,-0.58,-0.55,0.00,0.48,0.44,0.41,0.37,0.34,0.30],
[5750,0.63,0.65,-0.62,-0.58,-0.55,-0.51,0.48,0.44,0.41,0.37,0.34,0.30],
[5859,0.63,0.65,-0.62,-0.58,-0.55,-0.51,0.00,0.44,0.41,0.37,0.34,0.30],
[6109,0.63,0.65,0.62,-0.58,-0.55,-0.51,-0.48,0.00,0.41,0.37,0.34,0.30],
[6328,0.63,0.65,0.62,0.58,-0.55,-0.51,-0.48,-0.44,0.00,0.37,0.34,0.30],
[6453,0.63,0.65,0.62,0.58,-0.55,-0.51,-0.48,-0.44,-0.41,0.00,0.34,0.30],
[6578,0.63,0.65,0.62,0.58,0.55,-0.51,-0.48,-0.44,-0.41,-0.37,0.00,0.00],
[6734,0.00,0.65,0.62,0.58,0.55,-0.51,-0.48,-0.44,-0.41,-0.37,-0.34,0.00]
]

servo_list = [0, 1, 2, 3, 4, 5, 6, 7]
servo_pos = [0, 0, 0, 0, 0, 0, 0, 0]
servo_step = [0, 0, 0, 0, 0, 0, 0, 0]

if len(servo_array) == 0:
   exit

for i in servo_list:
      servo_step[i] = int((servo_array[0][i + 1] * scale * 2.0) / swing_steps)
      if servo_step[i] < 0:
         servo_step[i] = -servo_step[i]

#robot_servo = Servo()

for step in servo_array:
    print("step=", step)
    for i in servo_list:
        v = 0
        if step[i + 1] > 0.0:
           v = servo_step[i]
           servo_pos[i] = servo_pos[i] + v
           if servo_pos[i] > max_angle:
              v = v - (servo_pos[i] - max_angle)
              servo_pos[i] = max_angle
        else:
            if step[i + 1] < 0.0:
               v = -servo_step[i];
               servo_pos[i] = servo_pos[i] + v
               if servo_pos[i] < -max_angle:
                  v = v + (-servo_pos[i] - max_angle)
                  servo_pos[i] = -max_angle
        #robot_servo.set_servo ((11 - i), servo_pos[i])
        print("i=", (11 - i), "v=", v, "pos=", servo_pos[i])
    #print(servo_pos)
    sleep(delay)




