import os 
Vtype = ['Constant', 'Linear1', 'Linear2', 'Inverse', 'InverseSquared']
Vexp = [0,1,1,-1,-2]
for i in range(0, len(Vtype)):
	if Vtype[i][-1] == 2:
		l = 2
	else:
		l = 1
	#title = "Effective Potential: " + Vtype[i]
	#print(title.split()[-1])
	os.system("python EffectivePotential.py --title "+Vtype[i]+" --Vexp "+str(Vexp[i])+ " --l "+str(l))
 
