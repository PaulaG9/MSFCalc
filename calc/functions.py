import pandas as pd 

def getNetPatients(numpatients, duration, monincrease):
            if duration/30>1:
                final_mth_patients=numpatients+(round(duration/30)-1)*monincrease
                net_patients=((numpatients+final_mth_patients)*round(duration/30))/2
            else:
                net_patients=numpatients+monincrease   
                         
            return net_patients

def getEstimate(net_patients, duration, frequency, units, packaging, packaging_size):
            if not packaging:
                 estimate=(net_patients * duration * frequency * units)
            elif packaging=='bottle':
                estimate=(net_patients * duration * frequency * units* 5)/packaging_size               
            else:
                estimate=(net_patients * duration * frequency * units)

            return estimate




