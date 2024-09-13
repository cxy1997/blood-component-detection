echo python -m torch.distributed.launch \
  --nproc_per_node=1 \
  --master_port=29500 \
  tools/analysis_tools/benchmark.py \
  configs/bond_models/$1.py \
  work_dirs/$1/latest.pth \
  --launcher pytorch
python -m torch.distributed.launch \
  --nproc_per_node=1 \
  --master_port=29500 \
  tools/analysis_tools/benchmark.py \
  configs/bond_models/$1.py \
  work_dirs/$1/latest.pth \
  --launcher pytorch