import os
from pathlib import Path 

os.chdir('C:/Users/leoki/2024')
for file in os.listdir():
 f = Path(file)
 #name, ext = os.path.splitext(file)
 name,ext = f.stem,f.suffix
 splitted = name.split("-")
 splitted = [s.strip() for s in splitted]
 new_name =f'{splitted[1].zfill(2)}-{splitted[0]}{ext}'
 print (new_name)
 #os.rename(file, new_name)
 f.rename(new_name)

