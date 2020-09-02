# DataBlender API for comments analysis

## Preliminary
###### Install *conda*
* Download the latest linux installer for miniconda at https://docs.conda.io/en/latest/miniconda.html. (python 3.7, 64-bits)
* In a terminal:
```
cd path/to/installer/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
```
*Note: replace file name to appropriate if using 32-bits system.*

###### Install *git*
```
sudo apt-get install git
```
## Install API
* Clone this repo:
```
git clone https://github.com/jahrardblender/analysecomment2
```
* Create and prepare conda environment:
```
conda env create -f environment.yml
```
* Download and unzip the French Sentiment Analysis model (https://drive.google.com/file/d/1q2wSuv45_npmcrHTQo2fNyIhb4qsHNIy/view?usp=sharing). It should be placed in a folder *pretrained_models*, where you will use the API.

## Sentence classification using comparison with list of topic related words

A demo can be seen by running demo_classif.py. It should be relatively self explanatory.

Be sure to have *ETUDE-25-06-20.xlsx* and *datablender_comments.sql* in a "Data/" directory in your folder to run the demo. These files can be found in teams.

## Sentiment Analysis for french comments

A demo can be seen by running demo_sentiment.py. It should be relatively self explanatory.
