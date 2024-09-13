_base_ = '../autoassign/autoassign_r50_fpn_8x2_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    bbox_head=dict(num_classes=3))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('MCF7', 'BEAD', 'RBC')
evaluation=dict(classwise=True, metric='bbox', iou_thrs=[0.75])
data = dict(
    samples_per_gpu=8,
    train=dict(
        img_prefix='data/bond2024/train2017/',
        classes=classes,
        ann_file='data/bond2024/annotations/instances_train2017.json'),
    val=dict(
        img_prefix='data/bond2024/val2017/',
        classes=classes,
        ann_file='data/bond2024/annotations/instances_val2017.json'),
    test=dict(
        img_prefix='data/bond2024/val2017/',
        classes=classes,
        ann_file='data/bond2024/annotations/instances_val2017.json'))
img_norm_cfg = dict(
    mean=[93.86357218127891] * 3,
    std=[15.443830719068398] * 3, to_rgb=True)