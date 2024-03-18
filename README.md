# USC BA estimator
Our architecture requires a freesurfer processed T1-weighted MRI scan as input to predict brain age. Users must first create the brain.mgz file using the FreeSurfer software, which is available for free at https://surfer.nmr.mgh.harvard.edu/. 

We have provided sample code in the "/main.ipynb" file to calculate BA for a sample subject. We recommend using Jupyter notebook to execute our code. Please note that this software is only valid for estimating the brain ages of individuals over the age of 21. For individuals under the age of 21, estimated brain ages may not be accurate. 

Direct all questions and comments to irimia@usc.edu.  Please acknowledge the original publication when using this code:

Yin, Chenzhong, et al. "Anatomically interpretable deep learning of brain age captures domain-specific cognitive impairment." Proceedings of the National Academy of Sciences 120.2 (2023): e2214634120.

# Install modules and packages required by 3D-CNN model
Click the **Applications** folder in your dock, then **Utilities**, then **Terminal**. 
Type the command after the dollar sign and hit enter:
```
$ pip install -r requirements.txt
```

