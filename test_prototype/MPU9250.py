# MPU6050 9-DoF Example Printout

from mpu9250_i2c import *
from os import system
from math import atan2, pi, degrees, sqrt
from gpiozero import CPUTemperature

time.sleep(1) # delay necessary to allow mpu9250 to settle

def dist(a,b):
    return sqrt((a*a)+(b*b))
 
def get_x_rotation(x,y,z):
    radians = atan2(x, dist(y,z))
    return degrees(radians)
 
def get_y_rotation(x,y,z):
    radians = atan2(y, dist(x,z))
    return degrees(radians)

print('recording data')
# while 1:
#     try:
#         ax,ay,az,wx,wy,wz,temp = mpu6050_conv() # read and convert mpu6050 data
#         mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data
#     except:
#         continue
#     
#     print('{}'.format('-'*60))
#     print('accel [g]:\t x = {:.2f},\t y = {:.2f},\t z = {:.2f}'.format(ax,ay,az))
#     print('gyro [dps]:\t  x = {:.2f},\t y = {:.2f},\t z = {:.2f}'.format(wx,wy,wz))
#     print('mag [uT]:\t x = {:.2f},\t y = {:.2f},\t z = {:.2f}'.format(mx,my,mz))
#     print('{}'.format('-'*60))
# 
#     ax_scaled = ax / 16384.0
#     ay_scaled = ay / 16384.0
#     az_scaled = az / 16384.0
#     
#     print("X Rotation: " , round(get_x_rotation(ax_scaled, ay_scaled, az_scaled)))
#     print("Y Rotation: " , round(get_y_rotation(ax_scaled, ay_scaled, az_scaled)))
#     print('lateral angle: {} degrees'.format(round(atan2(my, mz)*180/pi)))
#     
#     
#     
# 
#     print('{}'.format('-'*60))
#     offset = 90-round(get_y_rotation(ax_scaled, ay_scaled, az_scaled))
# ##  print('stabilized lateral angle: {} degrees'.format(round(atan2(my, mz)*180/pi)-offset))
#     print('MPU 92/65 temperature {} C'.format(temp))
# 
#     cpu = CPUTemperature()
#     print('CPU Temperature {} \t degrees C'.format(cpu.temperature))
#     
#     time.sleep(0.5)
#     system('clear')
    
def gyro_data():
    ax,ay,az,wx,wy,wz,temp = mpu6050_conv() # read and convert mpu6050 data
    mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data
    
    ax_scaled = ax / 16384.0
    ay_scaled = ay / 16384.0
    az_scaled = az / 16384.0
    
    x_rotation = round(get_x_rotation(ax_scaled, ay_scaled, az_scaled))
    y_rotation = round(get_y_rotation(ax_scaled, ay_scaled, az_scaled))
    angle      = (round(atan2(my, mz)*180/pi))
    
    gyro_temp = round(temp,2)
    
    cpu = CPUTemperature()
    cpu_temp = round(cpu.temperature,2)
    
    return x_rotation, y_rotation, angle, gyro_temp, cpu_temp
