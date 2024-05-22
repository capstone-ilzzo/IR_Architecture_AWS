# Artifact-Acquisition
침해 사고가 발생한 환경의 아티팩트를 수집하는 과정은 다음과 같은 Python 기반의 lamda 함수를 통해 자동화하고 있다.

0. 0-GuardDuty-Forensic-Discord-Alarm.py
1. 1-Lime-auto.py
2. 2-EC2-Exec-With-SSM.py
3. 3-AMI-Snapshot.py
---
## 0. 0-GuardDuty-Forensic-Discord-Alarm.py
아티팩트 채증 자동화 Step Function이 실행되면 가장 먼저 실행되는 함수로 본격적인 채증이 시작되기 전 SNS인 Slack으로 알림을 보내는 역할을 한다.
## 1. 1-Lime-auto.py
본격적인 채증을 시작하는 함수로 메모리 덤프로 휘발성 아티팩트를 수집하고 이를 S3에 저장하는 역할을 한다.
## 2. 2-EC2-Exec-With-SSM.py
이전 Step에서 수집한 아티팩트 이외의 로그, 네트워크, 히스토리와 같은 정보를 수집하는 역할을 한다.
## 3. 3-AMI-Snapshot.py
비휘발성 아티팩트 수집의 역할을 하는 함수로 비휘발성 아티팩트 수집을 위해 EC2 운영체제, 설정값, 디스크 스냅샷 등이 저장된 AMI를 저장한다.
