# Liver Tumor Detection DS3
## Ali Alani, Nathaphat Taleongpong, Samuel Lee
### Intro:

Problem:
- Locate tumors in CT scans of the liver

Project Solution:
- using Segmentation Learning [Semantic Segmentation] on a dataset of CT scans to train a UNET convolutional model.

### Data Collecting and Cleaning

The dataset we were provided with was
[Dataset](https://www.kaggle.com/datasets/modaresimr/medical-image-segmentation):

This dataset had files seperating ground truth files and raw CT scans. The ground truth are files that have been checked by radiologists.

We converted all the CT scan files into slices of PNG files, making sure to keep the same size and to check for any wrong or missing files.

- The liver files had 83 pairs of ground truth files(.pkl) and raw CT files (.nii)
- CT scans produce many hundreds of 2 dimensional images layered together that produce a 3D scan

### Model Used

We selected U-NET as our model after researching what past medical segmentation projects have done we found that U-NET is very well known for this.

#### Model Training

We trained out dataset but splitting the cleaned up data into training and validation. As well as using a MSE loss function.

### Results

Our model received an accuracy of 68% on the evaluation dataset, we found that computational power, the overall complexity of liver tumors and also the imaging conditions played a role in us not having a higher accuracy.


### GUI

https://a3alani-tumorous-gui-j8owgj.streamlit.app/

### Built Using:
- JupyturHub
- Python
- Streamlit (GUI)
- [Evalseg](https://pypi.org/project/evalseg/)



### Poster

<img width="1023" alt="Screenshot 2023-06-05 at 6 51 44 PM" src="https://github.com/a3alani/tumorous/assets/103146838/54734924-f8b9-40e3-9b01-9462e179a7da">






