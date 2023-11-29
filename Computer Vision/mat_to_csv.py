import scipy.io
import numpy as np
import pandas as pd
from pathlib import Path


pathlist = Path(r'C:\Users\Brandon L\CMP445\CMPSC445\Computer Vision\validationdata_mat').glob('**/*.mat')
for path in pathlist:
    path_str = str(path)
    
    data = scipy.io.loadmat(path_str)
    
    cols=[]
    for i in data:
          if '__' not in i:
              cols.append(i)
    temp_df = pd.DataFrame(columns=cols)
    for i in data:
         if '__' not in i:
              temp_df[i]=(data[i]).ravel()
    temp_df.to_csv(r'C:\Users\Brandon L\CMP445\CMPSC445\Computer Vision\validationdata_csv\{fname}.csv'.format(fname = path.stem))







