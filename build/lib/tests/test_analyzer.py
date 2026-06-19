"""야구 분석 패키지의 기능 및 예외 처리를 검증하는 pytest 단위 테스트 모듈입니다."""

import pytest
from baseball_analyzer import Batter, Pitcher


# ==================== [정상 케이스: 5건] ====================

def test_batter_profile_generation():
    """타자 생성 시 부모 클래스의 프로필 문자열이 올바르게 반환되는지 테스트합니다."""
    batter = Batter(name="구자욱", team="삼성")
    assert batter.get_profile() == "[삼성] 구자욱 (출장: 0경기)"


def test_batter_record_and_calculation():
    """타자의 경기 기록이 누적되고 타율(AVG)이 정확히 계산되는지 테스트합니다."""
    batter = Batter(name="김도영", team="기아")
    # 10타수 4안타 기록
    batter.record_at_bat(hits=4, walks=1, at_bats=10)
    assert batter.batting_average == 0.400
    assert batter.games_played == 1


def test_pitcher_record_and_era_calculation():
    """투수의 경기 기록이 누적되고 방어율(ERA)이 정확히 계산되는지 테스트합니다."""
    pitcher = Pitcher(name="원태인", team="삼성")
    # 9이닝 동안 3자책점 기록
    pitcher.record_pitch(innings=9.0, earned_runs=3)
    assert pitcher.earned_run_average == 3.00


def test_player_games_played_increment():
    """update_games 메서드 호출 시 출장 경기 수가 정상적으로 증가하는지 테스트합니다."""
    batter = Batter(name="홍창기", team="LG")
    batter.update_games(5)
    assert batter.games_played == 5


def test_multiple_records_accumulation():
    """여러 경기의 데이터가 누적되어도 비율이 정확히 계산되는지 테스트합니다."""
    batter = Batter(name="손아섭", team="NC")
    batter.record_at_bat(hits=2, walks=1, at_bats=5)  # 1차 경기
    batter.record_at_bat(hits=1, walks=0, at_bats=5)  # 2차 경기
    assert batter.at_bats == 10
    assert batter.hits == 3
    assert batter.batting_average == 0.300


# ==================== [엣지 케이스: 3건] ====================

def test_batter_zero_division_safety():
    """[엣지 케이스] 타수가 0일 때 ZeroDivisionError 없이 0.000을 반환하는지 테스트합니다."""
    batter = Batter(name="신인선수", team="한화")
    # 아무 기록도 없는 상태
    assert batter.batting_average == 0.000


def test_invalid_negative_input_raises_error():
    """[엣지 케이스] 음수 데이터가 입력되었을 때 ValueError를 올바르게 발생시키는지 테스트합니다."""
    batter = Batter(name="로하스", team="KT")
    with pytest.raises(ValueError):
        batter.record_at_bat(hits=-1, walks=0, at_bats=10)


def test_impossible_hits_raises_error():
    """[엣지 케이스] 안타 수가 타수보다 많은 모순된 데이터 입력 시 에러를 내는지 테스트합니다."""
    batter = Batter(name="페디", team="NC")
    with pytest.raises(ValueError):
        # 5타수인데 6안타를 치는 것은 불가능
        batter.record_at_bat(hits=6, walks=0, at_bats=5)
        