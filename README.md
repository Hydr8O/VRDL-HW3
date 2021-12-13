Reproducing submission
=======================
1. Clone repository git clone https://github.com/Hydr8O/VRDL-HW3
2. Install dependencies pip install -r requirements.txt
3. Install mish-cuda by running install_mishcuda.sh
4. Download pretrained model https://drive.google.com/file/d/1J3jBq2LOCaGSDtFmIq1YXcpx4tOzYsYs/view?usp=sharing
5. Put the weights into weights folder like weights/*.pt
6. Put images for inference into test/*.jpg
7. Launch inference with python inference.py
8. python sort_json.py to sort predictions. The output will be in answer.json
