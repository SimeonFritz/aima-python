from ev3dev.auto import OUTPUT_D, LargeMotor
import time
right = LargeMotor(OUTPUT_D)

#move the arm down
right.run_timed(speed_sp = 360, time_sp = 600)
time.sleep(1)