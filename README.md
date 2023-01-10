# USC BA estimator
We provide Python code to estimate brain age (BA) from a raw T1-weighted MRI scan (brain.mgz file). Our architecture takes as input a T1-weighted MRI scan and processes it as described in the original publication. Sample code to calculate BA in a sample subject is provided in "/3D-CNN/ONNX_demo.ipynb". Our onnx files, which contain the compressed model architecture, are in the Models folder. We suggest using Google Colab or Jupyter notebook to execute our code. This software is valid for estimating the brain ages of persons whose chronological age is over 20. For persons under age 21, estimated brain ages may not be accurate. Direct all questions and comments to irimia.laboratory@gmail.com.  Please acknowledge the original publication when using this code:

Yin, Chenzhong, et al. "Anatomically interpretable deep learning of brain age captures domain-specific cognitive impairment." Proceedings of the National Academy of Sciences 120.2 (2023): e2214634120.

