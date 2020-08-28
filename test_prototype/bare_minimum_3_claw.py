from roboclaw_3 import Roboclaw

#Linux comport name
rc = Roboclaw("/dev/ttyACM0",115200)

rc.Open()
print("-----------------------------------------------------------")
if rc.Open() == 0:
    print("No roboclaw found on the comport\n")
else:
    print("Roboclaw connected\n")

name = ['claw', 'claw_2', 'claw_3']
address = [128, 129, 130]

for i in range(3):
    try:
        print('\t'.join((name[i], 'set up', str(rc.ReadError(address[i])))))
    except:
        print('\t'.join((name[i], "not found")))
print("-----------------------------------------------------------")

def pitchStop():
    rc.SpeedM1(128, 0)

def rotationStop():
    rc.SpeedM2(128, 0)

def columnStop():
    rc.SpeedM1(129, 0)

def launchStop():
    rc.SpeedM2(129, 0)

def caseStop():
    rc.SpeedM1M2(130, 0, 0)

def allStop():
    for i in address:
        rc.SpeedM1M2(i, 0, 0)

def pitchEnc():
    print(rc.ReadEncM1(128))

def rotationEnc():
    print(rc.ReadEncM2(128))

def columnEnc():
    print(rc.ReadEncM1(129))

def launchEnc():
    print(rc.ReadEncM2(129))

def caseRightEnc():
    print(rc.ReadEncM1(130))

def caseLeftEnc():
    print(rc.ReadEncM2(130))

def pitchSet(x):
    rc.SetEncM1(128, x)
    print('\t'.join(('Updated encoder value: ', rc.ReadEncM1(128))))

def rotationSet(x):
    rc.SetEncM2(128, x)
    print('\t'.join(('Updated encoder value: ', rc.ReadEncM2(128))))

def columnSet(x):
    rc.SetEncM1(129, x)
    print('\t'.join(('Updated encoder value: ', rc.ReadEncM1(129))))

def launchSet(x):
    rc.SetEncM2(129, x)
    print('\t'.join(('Updated encoder value: ', rc.ReadEncM2(129))))

def caseSet(x):
    rc.SetEncM1(130, x)
    rc.SetEncM2(130, x)
    print('\t'.join(('Updated encoder value: ', rc.ReadEncM1(130), rc.ReadEncM2(130))))

data = """
pitch_pulses                =   355000           
pitch_length                =   90.0             
pitch_speed_pulses          =   7000       
pitch_speed_manual          =   50         
pitch_ready                 =   80.0              

rotation_pulses             =   950000        
rotation_length             =   180.0         
rotation_speed_pulses       =   16000   
rotation_speed_manual       =   15      
rotation_ready              =   5.0           

lift_pulses                 =   19000             
lift_length                 =   130.0             
lift_speed_pulses           =   420         
lift_speed_manual           =   127         
lift_ready                  =   lift_length        

launch_pulses               =   14800           
launch_length               =   111.0           
launch_speed_pulses         =   6*13400   
launch_speed_pulses_slow    =   2500 
launch_speed_manual         =   40        
launch_acceleration         =   (launch_speed_pulses**2)/13400 
launch_max_speed            =   10           
launch_min_speed            =   1            
launch_max_acceleration     =   48    
launch_min_acceleration     =   1     
launch_standby              =   8000           
launch_mount                =   17000            
launch_break                =   21000            
launch_bottom               =   0               
launch_connect              =   2190 
"""
print(data)
