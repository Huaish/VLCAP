#!/usr/bin/env bash
res_dir=$1
split_name=$2
data_path=$3
out_dir=$4
output=$5
python src/translate.py \
--res_dir=results/${res_dir} \
--eval_splits=${split_name} \
--data_path=${data_path} \
--out_dir=${out_dir} \
--output=${output} \
${@:6}
