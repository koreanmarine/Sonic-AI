# Sonic-AI("Real-Time Emergency Textualization")
### STT 모델과 LLM 모델을 결합한  Sonic - AI
- AI 기반의 사운드를 통한 실시간 위급상황 감지 및 분석 & 텍스트 보고
- ("AI-Based Real-Time Emergency Detection & Analysis Through Sound with Text Reporting")
  
### 프로젝트 개요
- 본 프로젝트는 인공지능(AI)을 활용하여 위급상황 발생 시 신속하게 그 상황을 감지하고 분석하는 모델을 개발하는 것을 목표로 하고 있습니다.
- 이 모델은 오디오 데이터를 분석하여 위급상황인지 아닌지를 판단하며, 판단된 상황을 텍스트로 변환하여 관할 경찰서나 지자체에 신속하게 보고합니다.

### 실제 모델 동작 순서
<img src = "https://github.com/koreanmarine/Sonic-AI/assets/130243045/93647c87-70b2-4a80-83bd-001e61f2a6ec" width="200" height="400"/>


### CCTV와 오디오 모니터링의 차이점
- CCTV 모니터링 시스템은 물리적인 사각지대와 외부 요인에 의해 성능이 제한될 수 있습니다.
- 반면, 오디오 모니터링은 이러한 물리적 제약사항이 적고, 좀 더 넓은 지역을 효과적으로 감시할 수 있습니다.

### 텍스트 변환의 장점
- 음성 또는 영상 데이터는 상황을 정확하게 파악하기 위해 전체를 철저히 검토해야 하지만, 텍스트 데이터는 이를 훨씬 더 빠르고 간편하게 할 수 있습니다.
- 따라서 본 모델의 텍스트 변환 기능은 관할 기관이 신속하고 정확하게 상황을 판단할 수 있도록 도와줍니다.
# 
## 데이터 설명
### 테스트용 데이터 
- https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=170)
![image](https://github.com/koreanmarine/Sonic-AI/assets/130243045/417d2a87-0831-4919-b5d9-0d9f9da81275)

## 성능 확인 데이터
- 성능확인 데이터는 직접 위험 상황 녹음 및 영화와 드라마에서 위험 상황을 추출하여 사용했습니다.
