_base_ = '../sparse_rcnn/sparse_rcnn_r101_fpn_300_proposals_crop_mstrain_480-800_3x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=[
            dict(
                type='DIIHead',
                num_classes=3,
                num_ffn_fcs=2,
                num_heads=8,
                num_cls_fcs=1,
                num_reg_fcs=3,
                feedforward_channels=2048,
                in_channels=256,
                dropout=0.0,
                ffn_act_cfg=dict(type='ReLU', inplace=True),
                dynamic_conv_cfg=dict(
                    type='DynamicConv',
                    in_channels=256,
                    feat_channels=64,
                    out_channels=256,
                    input_feat_shape=7,
                    act_cfg=dict(type='ReLU', inplace=True),
                    norm_cfg=dict(type='LN')),
                loss_bbox=dict(type='L1Loss', loss_weight=5.0),
                loss_iou=dict(type='GIoULoss', loss_weight=2.0),
                loss_cls=dict(
                    type='FocalLoss',
                    use_sigmoid=True,
                    gamma=2.0,
                    alpha=0.25,
                    loss_weight=2.0),
                bbox_coder=dict(
                    type='DeltaXYWHBBoxCoder',
                    clip_border=False,
                    target_means=[0., 0., 0., 0.],
                    target_stds=[0.5, 0.5, 1., 1.])) for _ in range(6)
        ]
    ))


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