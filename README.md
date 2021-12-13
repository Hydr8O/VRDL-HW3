Reproducing submission
=======================
1. Clone repository git clone https://github.com/Hydr8O/VRDL-HW3
2. Create conda environment conda create -n hw3_env python=3.7 -y
3. Activate environment conda activate hw3_env
4. Install dependencies ./install.sh
6. Download pretrained model https://drive.google.com/file/d/1J3jBq2LOCaGSDtFmIq1YXcpx4tOzYsYs/view?usp=sharing
7. Put the weights into weights folder like weights/*.pt
8. Put images for inference into test/*.jpg
9. Launch inference with python inference.py
10. python sort_json.py to sort predictions. The output will be in answer.json
