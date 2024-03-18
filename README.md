# USC BA estimator
We provide Python code to estimate brain age (BA) from a raw T1-weighted MRI scan (brain.mgz file). Users will first need to create the brain.mgz file using FreeSurfer software, which is freely available at https://surfer.nmr.mgh.harvard.edu/. Our architecture takes as input a T1-weighted MRI scan and predicts brain age.

Sample code to calculate BA in a sample subject is provided in "/function/3D_CNN.ipynb". Our weight file, which contain the compressed model architecture, are in the "/model" folder. We suggest Jupyter notebook to execute our code. This software is valid for estimating the brain ages of persons whose chronological age is over 21. For persons under age 21, estimated brain ages may not be accurate. Direct all questions and comments to irimia@usc.edu.  Please acknowledge the original publication when using this code:

Yin, Chenzhong, et al. "Anatomically interpretable deep learning of brain age captures domain-specific cognitive impairment." Proceedings of the National Academy of Sciences 120.2 (2023): e2214634120.

# Install modules and packages required by 3D-CNN model
Click the **Applications** folder in your dock, then **Utilities**, then **Terminal**. 
Type the command after the dollar sign and hit enter:
```
$ pip install -r requirements.txt
```

