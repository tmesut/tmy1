
# coding: utf-8

# In[1]:


import os
import shutil

ligand = "/truba/home/iakgun/TMY/pdbqt_2/"

res = "/truba/home/iakgun/TMY/receptor/hivpr_1/"

ligand_list = os.listdir(ligand)
ligand_list.sort()

print (ligand_list)

with open (res + "box_1.txt", "r") as dosya_1:
    satirlar=dosya_1.readlines()    

for j in range(0,len(ligand_list)):   
    dos_1 = res + ligand_list[j][:-6]
    os.mkdir(dos_1)
    shutil.copy(ligand + ligand_list[j], dos_1)
    
    with open (dos_1 + "/config_"+ ligand_list[j][:-6] + ".txt", "a") as dosya_2:
        dosya_2.write("receptor = "  + res  + "res/receptor.pdbqt\n")
        dosya_2.write("ligand = "  + dos_1 + "/" + ligand_list[j]  + "\n")
        dosya_2.write(satirlar[0] + satirlar[1]+ satirlar[2]+ satirlar[3]+ satirlar[4]+ satirlar[5]+"\n")
        dosya_2.write("out = "  + dos_1 + "/docked." + ligand_list[j][:-6] + ".pdbqt\n" )
        dosya_2.write("log = "  + dos_1 + "/log." + ligand_list[j][:-6] + ".txt\n")
        dosya_2.write("num_modes = 1\n")
        dosya_2.write("cpu = 8\n")
    os.chdir(dos_1)
    os.system("/truba/home/iakgun/vina/./qvina --config config_" + ligand_list[j][:-6] + ".txt")

shutil.make_archive(res, 'zip', res)
shutil.rmtree(res)

