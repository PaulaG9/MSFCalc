import pandas as pd 

def getNetPatients(numpatients, duration, monincrease, attrrate):
            if duration/30>1:
                final_mth_patients=numpatients+(round(duration/30)-1)*(monincrease-attrrate)
                net_patients=((numpatients+final_mth_patients)*round(duration/30))/2
            else:
                net_patients=numpatients+(monincrease-attrrate)            
            return net_patients

def getEstimate(net_patients, duration, frequency):

            estimate=net_patients * duration * frequency

            return estimate


