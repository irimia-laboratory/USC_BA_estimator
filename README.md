# USC_BA_estimator
# 3D-CNN BA estimator
Example code for estimating brain age (BA) value from a raw T1-weighted MRI scan (brain.mgz file). The code package is available in Python. Run code in Google Colab is recommended.
## Data preprocessing
Our architecture takes T1-weighted MRI scan (<img src="http://chart.googleapis.com/chart?cht=tx&chl=256\times256\times256" style="border:none;">), than rescale it to numpy matrices <img src="http://chart.googleapis.com/chart?cht=tx&chl=82\times86\times100" style="border:none;"> for males and <img src="http://chart.googleapis.com/chart?cht=tx&chl=80\times82\times96" style="border:none;"> for females. The example code for data preprocessing is shown in "/3D-CNN/data_preprocess.ipynb".
## BA estimation model 
3D-CNN is trained on 4,678 cognitively normal (CN) participants (mean age:59.1, age range: 22-95) from publicly available repositories (UK Biobank (UKBB), Human Con-
nectome Project-Aging (HCP-A), Human Connectome Project-Young Adult (HCP-YA), and CNs in Alzheimer’s Disease Neuroimaging Initiative (ADNI)) and test on 1170 CN participants. A distinct 3D-CNN was trained for each sex to estimate participants’ ages. Our models are validated via transfer learning which are tested on CamCAN, MCI and AD patients in ADNI without fine-tuning. The example architectures are shown in "/3D-CNN/ONNX_demo.ipynb" and the model. The onnx files for males and females are stored in "/Models/". 
## Data availability
We provide example numpy arrays to execute our code (brain volumn for 10 CN males and 10 CN females) in "data" folder. Feel free to leave feedbacks and ask questions. We want to make the repository helpful for your research.
