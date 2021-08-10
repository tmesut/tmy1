
# coding: utf-8

# In[1]:


import os
import shutil

ligand = "/truba/home/iakgun/TMY/pdbqt/"

res = "/truba/home/iakgun/TMY/receptor/"

son = "/truba/home/iakgun/TMY/results/"

ligand_list = os.listdir(ligand)
ligand_list.sort()
res_list = os.listdir(res)
res_list.sort()

print (ligand_list)
print(res_list)

for i in range (0,len(res_list)):
    local_list = os.listdir(res + res_list[i])    
    local = [local_list[g] for g in range (0,len(local_list)) if local_list[g][-6:] == '.pdbqt'][0]
    print(local)

    
    with open (res + res_list[i] + "/" + "box_1.txt", "r") as dosya_1:
        satirlar=dosya_1.readlines()
    
    for j in range(0,len(ligand_list)):   
        dos_1 = res + res_list[i] + "/" + ligand_list[j][:-6]
        print(dos_1)
        os.mkdir(dos_1)
        shutil.copy(ligand + ligand_list[j], dos_1)
        with open (dos_1 + "/config_"+ ligand_list[j][:-6] + ".txt", "a") as dosya_2:
            dosya_2.write("receptor = "  + res + res_list[i] + "/res/receptor.pdbqt\n")
            dosya_2.write("ligand = "  + dos_1 + "/" + ligand_list[j]  + "\n")
            dosya_2.write(satirlar[0] + satirlar[1] + satirlar[2]+ satirlar[3]+ satirlar[4]+ satirlar[5] + "\n")
            dosya_2.write("out = "  + dos_1 + "/docked." + ligand_list[j][:-6] + ".pdbqt\n" )
            dosya_2.write("log = "  + dos_1 + "/log." + ligand_list[j][:-6] + ".txt\n")
            dosya_2.write("num_modes = 1\n")
            dosya_2.write("cpu = 8\n")
        os.chdir(dos_1)
        os.system("/truba/home/iakgun/vina/./qvina --config config_" + ligand_list[j][:-6] + ".txt")
        
    dos_2 = res + res_list[i] + "/" + local[:-6]
    os.mkdir(dos_2)
    shutil.copy(res + res_list[i] + "/" + local, dos_2)
    with open (dos_2 + "/config_"+ local[:-6] + ".txt", "a") as dosya_3:
        dosya_3.write("receptor = "  + res + res_list[i] + "/res/receptor.pdbqt\n")
        dosya_3.write("ligand = "  + dos_2 + "/" + local[:-6] + ".pdbqt\n")
        dosya_3.write(satirlar[0] + satirlar[1] + satirlar[2]+ satirlar[3]+ satirlar[4]+ satirlar[5] + "\n")
        dosya_3.write("out = "  + dos_2 + "/docked." + local[:-6] + ".pdbqt\n" )
        dosya_3.write("log = "  + dos_2 + "/log." + local[:-6] + ".txt\n")
        dosya_3.write("num_modes = 1\n")
        dosya_3.write("cpu = 8\n")
    os.chdir(dos_2)
    os.system("/truba/home/iakgun/vina/./qvina --config config_" + local[:-6] + ".txt")
    
    dos_3 = res + res_list[i] + "/" + local[:-6] + "_loc"
    os.mkdir(dos_3)
    shutil.copy(res + res_list[i] + "/" + local, dos_3)
    with open (dos_3 + "/config_"+ local[:-6] + "_loc"+ ".txt", "a") as dosya_4:
        dosya_4.write("receptor = " + res + res_list[i] + "/res/receptor.pdbqt\n")
        dosya_4.write("ligand = "  + dos_3 + "/" + local[:-6] + ".pdbqt\n")
        dosya_4.write(satirlar[0] + satirlar[1] + satirlar[2]+ satirlar[3]+ satirlar[4]+ satirlar[5] + "\n")
        dosya_4.write("out = "  + dos_3 + "/docked." + local[:-6] + "_loc.pdbqt\n" )
        dosya_4.write("log = "  + dos_3 + "/log." + local[:-6] + "_loc.txt\n")
        dosya_4.write("num_modes = 1\n")
        dosya_4.write("cpu = 8\n")
    os.chdir(dos_3)
    os.system("/truba/home/iakgun/vina/./qvina --config config_" + local[:-6] + "_loc.txt --local_only")
    os.chdir(son)

    shutil.move(res + res_list[i], son)

