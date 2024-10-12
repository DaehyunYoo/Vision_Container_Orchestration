# Image Segmentation with PyTorch and Kubernetes

## 프로젝트 개요

이 프로젝트는 PyTorch를 사용한 이미지 세그멘테이션 모델을 Docker 컨테이너로 패키징하고 Kubernetes 클러스터에 배포하는 과정을 보여주는 토이 프로젝트입니다. 이 프로젝트는 컴퓨터 비전, Docker, 그리고 Kubernetes를 학습하고 실습하기 위한 목적으로 만들어졌습니다.

## 기술 스택

- Python 3.8+
- PyTorch
- FastAPI
- Docker
- Kubernetes

## 프로젝트 구조

```
image-segmentation-k8s/
│
├── src/
│   ├── app.py
│   ├── model.py
│   └── utils.py
│
├── kubernetes/
│   └── deployment.yaml
│
├── Dockerfile
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

## 설치 및 실행 방법

1. 저장소 클론:
   ```
   git clone https://github.com/your-username/image-segmentation-k8s.git
   cd image-segmentation-k8s
   ```

2. 필요한 Python 패키지 설치:
   ```
   pip install -r requirements.txt
   ```

3. Docker 이미지 빌드:
   ```
   docker build -t your-docker-registry/image-segmentation:v1 .
   ```

4. Docker 이미지 푸시 (선택사항):
   ```
   docker push your-docker-registry/image-segmentation:v1
   ```

5. Kubernetes 배포:
   ```
   kubectl apply -f kubernetes/deployment.yaml
   ```

## API 사용법

API 엔드포인트: `/segment/`

이미지 세그멘테이션을 위해 POST 요청을 보내세요:

```python
import requests

url = "http://your-service-ip/segment/"
files = {"file": open("path/to/your/image.jpg", "rb")}
response = requests.post(url, files=files)

print(response.json())
```

응답은 base64로 인코딩된 세그멘테이션 마스크를 포함합니다.

## 개발 노트

- 이 프로젝트는 학습 목적으로 만들어졌으며, 프로덕션 환경에서 사용하기 위해서는 추가적인 보안 조치와 최적화가 필요합니다.
- 클라우드 환경에서 실행할 경우, 해당 클라우드 제공업체의 가이드라인을 참조하세요.