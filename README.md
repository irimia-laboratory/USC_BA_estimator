# USC_BA_estimator
# 3D-CNN BA estimator
Example code for estimating brain age (BA) value from a raw T1-weighted MRI scan (brain.mgz file). The code is available in Python. Running the code in Google Colab is recommended. Please acknowledge the original publication when using this code:
<CITATION>
## Data preprocessing
Our architecture takes as input a T1-weighted MRI scan of size <img src="http://chart.googleapis.com/chart?cht=tx&chl=256\times256\times256" style="border:none;"> and reformats it as a numpy matrix of size <img src="http://chart.googleapis.com/chart?cht=tx&chl=82\times86\times100" style="border:none;">. The example code for data preprocessing is in "/3D-CNN/data_preprocess.ipynb".
## BA estimation model 
The 3D-CNN is trained on 4,678 cognitively normal (CN) participants (mean age:59.1, age range: 22-95) from publicly available repositories (UK Biobank (UKBB), Human Con-
nectome Project-Aging (HCP-A), Human Connectome Project-Young Adult (HCP-YA), and the Alzheimer’s Disease Neuroimaging Initiative (ADNI)). The CNN was tested on 1170 CN participants. Our models were validated via transfer learning without fine-tuning on CN participants from CamCAN and ADNI. Sample architectures are shown in "/3D-CNN/ONNX_demo.ipynb". The onnx files are stored in "/Models/". We suggest using Google Colab or Jupyter notebook to execute our code. 
## Help
Direct all questions and comments to irimia.laboratory@gmail.com. 
