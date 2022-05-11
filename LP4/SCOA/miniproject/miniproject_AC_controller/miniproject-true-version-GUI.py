import skfuzzy as fuzzy
import skfuzzy
from skfuzzy import control as ctrl
import numpy as np
import tkinter as tk
  
root = tk.Tk()
 
# setting the windows size
root.geometry("600x400")

#Setting Input Attributes
temp = ctrl.Antecedent(np.arange(16,31,1),'temp')
t_dif = ctrl.Antecedent(np.arange(-1,3,0.1),'t_dif')
d_point = ctrl.Antecedent(np.arange(10,18,1),'dew')
e_volt = ctrl.Antecedent(np.arange(130,220,10),'ev')

#Setting Input Membership Functions
#Membership Function values for temperature
temp['low'] = fuzzy.trapmf(temp.universe,[16,16,22,25])
temp['medium'] = fuzzy.trimf(temp.universe,[22,25,28])
temp['high'] = fuzzy.trapmf(temp.universe,[25,28,30,30])
#Membership Function values for temperature difference
t_dif['negative'] = fuzzy.trimf(t_dif.universe,[-1,-1,0])
t_dif['zero'] = fuzzy.trimf(t_dif.universe,[-0.5,0,0.5])
t_dif['positive'] = fuzzy.trimf(t_dif.universe,[0,1,2])
t_dif['large'] = fuzzy.trapmf(t_dif.universe,[1,2,3,3])
#Membership Function values for Dew Point
d_point['optimal'] = fuzzy.trapmf(d_point.universe,[10,10,11,14])
d_point['humid'] = fuzzy.trapmf(d_point.universe,[12,15,18,18])
#Membership Function values for Electric Volt
e_volt['low'] = fuzzy.trapmf(e_volt.universe,[130,130,160,180])
e_volt['high'] = fuzzy.trapmf(e_volt.universe,[170,190,220,220])


#Setting Output Attributes
c_speed = ctrl.Consequent(np.arange(0,110,10),'comp_speed')
f_speed = ctrl.Consequent(np.arange(0,110,10),'fan_speed')
mo = ctrl.Consequent(np.arange(0,1.1,0.1),'mo')
f_dir = ctrl.Consequent(np.arange(0,100,10),'f_dir')

#Setting Output Membership Functions
#Membership Function Values for Compressor Speed
c_speed['low'] = fuzzy.trapmf(c_speed.universe,[0,0,30,50])
c_speed['medium'] = fuzzy.trimf(c_speed.universe,[40,60,80])
c_speed['fast'] = fuzzy.trapmf(c_speed.universe,[70,90,100,100])
#Membership Function Values for Fan Speed
f_speed['low'] = fuzzy.trapmf(f_speed.universe,[0,0,30,50])
f_speed['medium'] = fuzzy.trimf(f_speed.universe,[40,60,80])
f_speed['fast'] = fuzzy.trapmf(f_speed.universe,[70,90,100,100])
#Membership Function for Mode of Operation
mo['ac'] = fuzzy.trimf(mo.universe,[0,1,1])
mo['de'] = fuzzy.trimf(mo.universe,[0,0,1])
#Membership Function Values for Fan Direction
f_dir['towards'] = fuzzy.trapmf(f_dir.universe,[0,0,40,70])
f_dir['away'] = fuzzy.trapmf(f_dir.universe,[40,70,90,90])

#Rules for Fuzzy
csr_list = []
rule_1 = ctrl.Rule(temp['low']&t_dif['negative']&d_point['optimal']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_1)
rule_2 = ctrl.Rule(temp['medium']&t_dif['negative']&d_point['optimal']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_2)
rule_3 = ctrl.Rule(temp['high']&t_dif['negative']&d_point['optimal']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_3)
rule_4 = ctrl.Rule(temp['low']&t_dif['zero']&d_point['optimal']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_4)
rule_5 = ctrl.Rule(temp['medium']&t_dif['zero']&d_point['optimal']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_5)
rule_6 = ctrl.Rule(temp['high']&t_dif['zero']&d_point['optimal']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_6)
rule_7 = ctrl.Rule(temp['low']&t_dif['positive']&d_point['optimal']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_7)
rule_8 = ctrl.Rule(temp['medium']&t_dif['positive']&d_point['optimal']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_8)
rule_9 = ctrl.Rule(temp['high']&t_dif['positive']&d_point['optimal']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_9)
rule_10 = ctrl.Rule(temp['low']&t_dif['large']&d_point['optimal']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_10)
rule_11 = ctrl.Rule(temp['medium']&t_dif['large']&d_point['optimal']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_11)
rule_12 = ctrl.Rule(temp['high']&t_dif['large']&d_point['optimal']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_12)
rule_13 = ctrl.Rule(temp['low']&t_dif['negative']&d_point['optimal']&e_volt['high'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_13)
rule_14 = ctrl.Rule(temp['medium']&t_dif['negative']&d_point['optimal']&e_volt['high'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_14)
rule_15 = ctrl.Rule(temp['high']&t_dif['negative']&d_point['optimal']&e_volt['high'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_15)
rule_16 = ctrl.Rule(temp['low']&t_dif['zero']&d_point['optimal']&e_volt['high'],[c_speed['low'],f_speed['fast'],mo['ac'],f_dir['towards']])
csr_list.append(rule_16)
rule_17 = ctrl.Rule(temp['medium']&t_dif['zero']&d_point['optimal']&e_volt['high'],[c_speed['low'],f_speed['medium'],mo['ac'],f_dir['towards']])
csr_list.append(rule_17)
rule_18 = ctrl.Rule(temp['high']&t_dif['zero']&d_point['optimal']&e_volt['high'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_18)
rule_19 = ctrl.Rule(temp['low']&t_dif['positive']&d_point['optimal']&e_volt['high'],[c_speed['fast'],f_speed['fast'],mo['ac'],f_dir['towards']])
csr_list.append(rule_19)
rule_20 = ctrl.Rule(temp['medium']&t_dif['positive']&d_point['optimal']&e_volt['high'],[c_speed['medium'],f_speed['medium'],mo['ac'],f_dir['towards']])
csr_list.append(rule_20)
rule_21 = ctrl.Rule(temp['high']&t_dif['positive']&d_point['optimal']&e_volt['high'],[c_speed['medium'],f_speed['medium'],mo['ac'],f_dir['towards']])
csr_list.append(rule_21)
rule_22 = ctrl.Rule(temp['low']&t_dif['large']&d_point['optimal']&e_volt['high'],[c_speed['fast'],f_speed['fast'],mo['ac'],f_dir['towards']])
csr_list.append(rule_22)
rule_23 = ctrl.Rule(temp['medium']&t_dif['large']&d_point['optimal']&e_volt['high'],[c_speed['fast'],f_speed['fast'],mo['ac'],f_dir['towards']])
csr_list.append(rule_23)
rule_24 = ctrl.Rule(temp['high']&t_dif['large']&d_point['optimal']&e_volt['high'],[c_speed['fast'],f_speed['fast'],mo['ac'],f_dir['towards']])
csr_list.append(rule_24)
rule_25 = ctrl.Rule(temp['low']&t_dif['negative']&d_point['humid']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_25)
rule_26 = ctrl.Rule(temp['medium']&t_dif['negative']&d_point['humid']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_26)
rule_27 = ctrl.Rule(temp['high']&t_dif['negative']&d_point['humid']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_27)
rule_28 = ctrl.Rule(temp['low']&t_dif['zero']&d_point['humid']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_28)
rule_29 = ctrl.Rule(temp['medium']&t_dif['zero']&d_point['humid']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_29)
rule_30 = ctrl.Rule(temp['high']&t_dif['zero']&d_point['humid']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_30)
rule_31 = ctrl.Rule(temp['low']&t_dif['positive']&d_point['humid']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_31)
rule_32 = ctrl.Rule(temp['medium']&t_dif['positive']&d_point['humid']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_32)
rule_33 = ctrl.Rule(temp['high']&t_dif['positive']&d_point['humid']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_33)
rule_34 = ctrl.Rule(temp['low']&t_dif['large']&d_point['humid']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_34)
rule_35 = ctrl.Rule(temp['medium']&t_dif['large']&d_point['humid']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_35)
rule_36 = ctrl.Rule(temp['high']&t_dif['large']&d_point['humid']&e_volt['low'],[c_speed['low'],f_speed['low'],mo['ac'],f_dir['away']])
csr_list.append(rule_36)
rule_37 = ctrl.Rule(temp['low']&t_dif['negative']&d_point['humid']&e_volt['high'],[c_speed['fast'],f_speed['fast'],mo['de'],f_dir['towards']])
csr_list.append(rule_37)
rule_38 = ctrl.Rule(temp['medium']&t_dif['negative']&d_point['humid']&e_volt['high'],[c_speed['low'],f_speed['low'],mo['de'],f_dir['away']])
csr_list.append(rule_38)
rule_39 = ctrl.Rule(temp['high']&t_dif['negative']&d_point['humid']&e_volt['high'],[c_speed['low'],f_speed['low'],mo['de'],f_dir['away']])
csr_list.append(rule_39)
rule_40 = ctrl.Rule(temp['low']&t_dif['zero']&d_point['humid']&e_volt['high'],[c_speed['fast'],f_speed['fast'],mo['de'],f_dir['towards']])
csr_list.append(rule_40)
rule_41 = ctrl.Rule(temp['medium']&t_dif['zero']&d_point['humid']&e_volt['high'],[c_speed['medium'],f_speed['fast'],mo['de'],f_dir['towards']])
csr_list.append(rule_41)
rule_42 = ctrl.Rule(temp['high']&t_dif['zero']&d_point['humid']&e_volt['high'],[c_speed['medium'],f_speed['medium'],mo['de'],f_dir['towards']])
csr_list.append(rule_42)
rule_43 = ctrl.Rule(temp['low']&t_dif['positive']&d_point['humid']&e_volt['high'],[c_speed['fast'],f_speed['fast'],mo['ac'],f_dir['towards']])
csr_list.append(rule_43)
rule_44 = ctrl.Rule(temp['medium']&t_dif['positive']&d_point['humid']&e_volt['high'],[c_speed['fast'],f_speed['fast'],mo['ac'],f_dir['towards']])
csr_list.append(rule_44)
rule_45 = ctrl.Rule(temp['high']&t_dif['positive']&d_point['humid']&e_volt['high'],[c_speed['medium'],f_speed['fast'],mo['ac'],f_dir['towards']])
csr_list.append(rule_45)
rule_46 = ctrl.Rule(temp['low']&t_dif['large']&d_point['humid']&e_volt['high'],[c_speed['fast'],f_speed['fast'],mo['ac'],f_dir['towards']])
csr_list.append(rule_46)
rule_47= ctrl.Rule(temp['medium']&t_dif['large']&d_point['humid']&e_volt['high'],[c_speed['fast'],f_speed['fast'],mo['ac'],f_dir['towards']])
csr_list.append(rule_47)
rule_48 = ctrl.Rule(temp['high']&t_dif['large']&d_point['humid']&e_volt['high'],[c_speed['fast'],f_speed['fast'],mo['ac'],f_dir['towards']])
csr_list.append(rule_48)

ac_ctrl = ctrl.ControlSystem(csr_list)

ac = ctrl.ControlSystemSimulation(ac_ctrl)

## GUI thkinter

temp_var=tk.StringVar()
t_dif_var=tk.StringVar()
dew_var = tk.StringVar()
ev_var = tk.StringVar()

comp_speed_var = tk.StringVar()
fan_speed_var = tk.StringVar()
f_dir_var = tk.StringVar()

def get_linguist(valmf,val,val_range):
    mf_keys = list(valmf.terms.keys())
    mf_value_list = []
    for i in range(len(mf_keys)):
        mf_value_list.append(skfuzzy.interp_membership(val_range,valmf[mf_keys[i]].mf,val))
    max_mf = max(mf_value_list)
    #print(mf_keys)
    #print(mf_value_list)
    ling_key = ''
    for i in range(len(mf_keys)):
        if max_mf == mf_value_list[i]:
            ling_key = mf_keys[i]
            break
    return ling_key

c_speed_range = np.arange(0,110,10)
f_speed_range = np.arange(0,110,10)
dir_range = np.arange(0,100,10)


def submit():
 
    temp = float(temp_var.get())
    t_dif = float(t_dif_var.get())
    dew = float(dew_var.get())
    ev = float(ev_var.get())
     
    print(f"The temp is : {temp}")
    print(f"The t_dif is : {t_dif}")
    print(f"The dew is : {dew}")
    print(f"The ev is : {ev}")

    ac.input['temp']  = temp
    ac.input['t_dif'] = t_dif
    ac.input['dew'] = dew
    ac.input['ev'] = ev
    ac.compute()

    comp_speed_var.set(get_linguist(c_speed,ac.output['comp_speed'],c_speed_range))
    fan_speed_var.set(get_linguist(f_speed,ac.output['fan_speed'],f_speed_range))
    f_dir_var.set(get_linguist(f_dir,ac.output['f_dir'],dir_range))

    print(ac.output['comp_speed'],ac.output['fan_speed'],ac.output['mo'],ac.output['f_dir'])
     
    #temp_var.set("")
    #t_dif_var.set("")
    #dew_var.set("")
    #ev_var.set("")

# creating a label for
# name using widget Label
temp_label = tk.Label(root, text = 'temp', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
temp_entry = tk.Entry(root,textvariable = temp_var, font=('calibre',10,'normal'))
  
# creating a label
t_dif_label = tk.Label(root, text = 't_dif', font = ('calibre',10,'bold'))
  
# creating a entry
t_dif_entry=tk.Entry(root, textvariable = t_dif_var, font = ('calibre',10,'normal'))

dew_label = tk.Label(root, text = 'dew', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
dew_entry = tk.Entry(root,textvariable = dew_var, font=('calibre',10,'normal'))
  
# creating a label
ev_label = tk.Label(root, text = 'ev', font = ('calibre',10,'bold'))
  
# creating a entry
ev_entry=tk.Entry(root, textvariable = ev_var, font = ('calibre',10,'normal'))

  
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)


comp_speed_label = tk.Label(root, text = 'comp_speed', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
comp_speed_entry = tk.Entry(root,textvariable = comp_speed_var, font=('calibre',10,'normal'))
  
# creating a label
fan_speed_label = tk.Label(root, text = 'fan_speed', font = ('calibre',10,'bold'))
  
# creating a entry
fan_speed_entry=tk.Entry(root, textvariable = fan_speed_var, font = ('calibre',10,'normal'))

f_dir_label = tk.Label(root, text = 'f_dir', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
f_dir_entry = tk.Entry(root,textvariable = f_dir_var, font=('calibre',10,'normal'))
  
# placing the label and entry in
# the required position using grid
# method
temp_label.grid(row=0,column=0)
temp_entry.grid(row=0,column=1)
t_dif_label.grid(row=1,column=0)
t_dif_entry.grid(row=1,column=1)
dew_label.grid(row=2,column=0)
dew_entry.grid(row=2,column=1)
ev_label.grid(row=3,column=0)
ev_entry.grid(row=3,column=1)

sub_btn.grid(row=5,column=1)

comp_speed_label.grid(row=7,column=0)
comp_speed_entry.grid(row=7,column=1)
fan_speed_label.grid(row=8,column=0)
fan_speed_entry.grid(row=8,column=1)
f_dir_label.grid(row=9,column=0)
f_dir_entry.grid(row=9,column=1)
  
# performing an infinite loop
# for the window to display
root.mainloop()