Reproducing submission
=======================
1. Clone repository git clone https://github.com/Hydr8O/VRDL-HW3
2. Create conda environment conda create -n hw3_env python=3.7 -y
3. Activate environment conda activate hw3_env
4. Install dependencies ./install.sh
6. Download pretrained model https://drive.google.com/file/d/1gs0ySEjGP6AAppdwTPVLgLqnPFIChi16/view?usp=sharing
7. Put images for inference into data/nucleus/test/images
8. Launch inference with python inference.py. The output will be in answer.segm.json
