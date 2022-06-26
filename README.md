# VLCap: Vision-Language with Contrastive Learning for Coherent Video Paragraph Captioning

In this paper, we leverage the human perceiving process, that involves vision and language interaction, to generate a coherent paragraph description of untrimmed videos. We propose vision-language (VL) features consisting of two modalities, i.e., (i) vision modality to capture global visual content of the entire scene and (ii) language modality to extract scene elements description of both human and non-human objects (e.g. animals, vehicles, etc), visual and non-visual elements (e.g. relations, activities, etc). Furthermore, we propose to train our proposed VLCap under a contrastive learning VL loss. The experiments and ablation studies on ActivityNet Captions and YouCookII datasets show that our VLCap outperforms existing SOTA methods on both accuracy and diversity metrics.


## Environment Setup
1. Clone this repository
```bash 
git clone https://github.com/UARK-AICV/VLCAP.git
cd VLCAP
```


2. Prepare Conda environment 

```bash
conda env create -f environment.yml
conda activate pytorch
```


3. Add project root to `PYTHONPATH`
> Note that you need to do this each time you start a new session.

```bash
source setup.sh
```

## Data Preparation
Download features from Google Drive: [env feature]() and [lang feature]().

```bash 
mkdir data/anet; cd data/anet
unzip anet_c3d
unzip anet_clip_b16
```


## Training

To train our MART model on ActivityNet Captions:
```
bash scripts/train.sh [anet/yc2] [true/false]
```
Here you can specify the dataset (ActivityNet:`anet` or YouCook2:`yc2`) and whether to use the proposed language feature (`true`/`false`).

Training log and model will be saved at `results/anet_re_*`.  
Once you have a trained model, you can follow the instructions below to generate captions. 

## Evaluation
1. Generate captions 
```
bash scripts/translate_greedy.sh anet_re_* [val/test]
```
Replace `anet_re_*` with your own model directory name. 
The generated captions are saved at `results/anet_re_*/greedy_pred_val.json`


2. Evaluate generated captions
```
bash scripts/eval.sh anet [val/test] results/anet_re_*/greedy_pred_val.json
```
The results should be comparable with the results we present at Table 5 of the paper. 

## Citations
If you find this code useful for your research, please cite our paper:

```bibtex
@inproceedings{kashu2020,
  title={VLCap: Vision-Language with Contrastive Learning for Coherent Video Paragraph Captioning},
  author={Kashu Yamazaki and Sang Truong and Khoa Vo and Michael Kidd and Chase Rainwater and Khoa Luu and Ngan Le},
  journal={ICIP},
  year={2022}
}
```

## Acknowledgement
We acknowledge the following open-source projects that we based on our work:

1. [MART](https://github.com/jayleicn/recurrent-transformer) 
