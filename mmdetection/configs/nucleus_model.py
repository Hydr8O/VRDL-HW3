_base_ = [
    "_base_/models/mask_rcnn_r50_fpn.py",
    "_base_/datasets/coco_instance.py",
]

dataset_type = "CocoDataset"
load_from = None
resume_from = None
classes = ("nucleus",)

# model settings
model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type="Pretrained", checkpoint="torchvision://resnet101"),
        frozen_stages=1,
    ),
    rpn_head=dict(
        anchor_generator=dict(scales=[8], ratios=[0.5, 1.0])
    ),
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)
    )
)

data = dict(
    samples_per_gpu=1,
    train=dict(
        type=dataset_type,
        ann_file="data/nucleus/train_annotations.json",
        classes=classes,
        img_prefix="data/nucleus/train/images",
    ),
    val=dict(
        type=dataset_type,
        ann_file="data/nucleus/test_annotations.json",
        classes=classes,
        img_prefix="data/nucleus/test/images",
    ),
    test=dict(
        type=dataset_type,
        ann_file="data/nucleus/test_annotations.json",
        classes=classes,
        img_prefix="data/nucleus/test/images",
    ),
)

checkpoint_config = dict(interval=1)

log_config = dict(interval=50, hooks=[dict(type="TextLoggerHook")])

custom_hooks = [dict(type="NumClassCheckHook")]

dist_params = dict(backend="nccl")
log_level = "INFO"


train_pipeline = [
    dict(type="Resize", img_scale=(800, 800), keep_ratio=True),
]

workflow = [("train", 1)]
optimizer = dict(type="SGD", lr=1e-3, momentum=0.9, weight_decay=0.0001)
runner = dict(type="EpochBasedRunner", max_epochs=450)
optimizer_config = dict(grad_clip=None)
lr_config = dict(
    policy="step",
    warmup="linear",
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[8, 11]
)
