from pathlib import Path

# How to use 
# Input in file directory
# And change the subfolder and parentfolder to match the sub and parent folder of the input dir
p_folder = "L"
s_folder = "Z"

for file in Path(r"C:\Users\Brandon L\CMP445\CMPSC445\HGM-4\HGM-1.0\{parentfolder}_CAM\{subfolder}".format(parentfolder=p_folder, subfolder=s_folder)).glob("*.xml"):
    file.rename(file.with_name("{fname}_{parentfolder}_{subfolder}.xml".format(fname = file.stem, parentfolder=p_folder, subfolder=s_folder)))