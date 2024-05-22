# Artifact-Analysis
침해 사고 수집 자동화 과정을 통해 수집된 아티팩트를 분석하는 과정은 다음과 같은 Python 기반의 lamda 함수를 통해 자동화하고 있다.

0. 0-Create-EC2.py
1. 1-Analysis-start.py
---
## 0. 0-Create-EC2.py
분석 과정의 전에 실행되는 함수로 분석 소프트웨어를 실행하여 수집한 아티팩트를 분석하는 기능을 하는 EC2를 생성하는 역할을 한다.
## 1. 1-Analysis-start.py
분석 EC2에서 analysis_software.py를 실행하여 volatility와 lambda를 이용해 분석을 진행한 후 결과를 S3에 저장하는 역할을 한다.
