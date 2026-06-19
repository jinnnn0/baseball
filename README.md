# ⚾ 야구 데이터 분석 및 경기 기록 추적기 (baseball_analyzer)

## 1. 프로젝트 개요
`baseball_analyzer`는 야구 선수(타자 및 투수)의 개인 경기 성적 데이터를 객체지향적인 설계 구조로 입력받아 세부 스탯(타자 - 타율, 투수 - 방어율 등)을 자동으로 계산하고 관리하는 Python 패키지입니다. 

## 2. 설치 방법
```bash
pip install .
```

## 3. 빠른 시작 코드 예시
```python
from baseball_analyzer import Batter, Pitcher
from baseball_analyzer.utils import clean_percentage

# 타자 기록 등록 및 타율 산출
batter = Batter(name="송찬의", team="엘지")
batter.record_at_bat(hits=3, walks=1, at_bats=10)
print(batter.get_profile())
print(f"타율: {clean_percentage(batter.batting_average)}")

# 투수 기록 등록 및 방어율 산출
pitcher = Pitcher(name="임찬규", team="엘지")
pitcher.record_pitch(innings=9.0, earned_runs=3)
print(pitcher.get_profile())
print(f"방어율(ERA): {pitcher.earned_run_average}")
```

## 4. 주요 기능 설명
객체지향 : 공통 정보를 처리하는 부모 클래스를 기반으로 상속 구조 설계 -> 중복 코드 제거
타자 통계 계산 : 누적 타수, 안타, 볼넷을 기반으로 타율(AVG) 계산
투수 통계 계산 : 소화한 이닝과 자책점을 기반으로 9이닝 기준 방어율(ERA) 계산
예외 및 안전장치 : 데이터 누락으로 분모가 0이 되는 상황을 비공개 메서드를 이용해 방어, 음수 데이터 입력 시 ValueError를 발생시킴
야구식 표기 전환 : 유틸리티 모듈을 통해 소수점 타율을 야구 표준 포맷(예 : 0.300 -> .300)으로 출력

## 5. 테스트 실행 방법
```
pytest
```

## 6. 작성자 정보
이름 : 정여진
학과 : 컴퓨터공학과
