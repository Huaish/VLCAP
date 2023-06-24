# Exploring CLIP-based Automated Approaches for Video Content Description Generation

## Environment Setup
1. Clone this repository
```bash 
git clone https://github.com/Huaish/VLCAP.git
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
Download features from Google Drive: [env feature](https://uark.box.com/s/01twnsrjxbf7d48wki5s5v43ri5p66vl) and [lang feature](https://uark.box.com/s/un9t7vv2l61u1541krqfxqro1t9hfkm4).

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
bash scripts/eval.sh anet [val/test] results/anet_re_*/greedy_pred_[val/test].json
```
The results should be comparable with the results we present at Table 5 of the paper. 

<!-- ## Citations
If you find this code useful for your research, please cite our papers:

```bibtex
@INPROCEEDINGS{9897766,
  author={Yamazaki, Kashu and Truong, Sang and Vo, Khoa and Kidd, Michael and Rainwater, Chase and Luu, Khoa and Le, Ngan},
  booktitle={2022 IEEE International Conference on Image Processing (ICIP)}, 
  title={VLCAP: Vision-Language with Contrastive Learning for Coherent Video Paragraph Captioning}, 
  year={2022},
  volume={},
  number={},
  pages={3656-3661},
  doi={10.1109/ICIP46576.2022.9897766}}

``` -->

## Acknowledgement
We acknowledge the following open-source projects that we based on our work:

1. [MART](https://github.com/jayleicn/recurrent-transformer) 
2. [VLCAP](https://github.com/UARK-AICV/VLCAP.git)
