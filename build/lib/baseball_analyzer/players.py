"""타자와 투수 등 포지션별 세부 클래스를 정의하는 모듈입니다."""

from baseball_analyzer.core import Player


class Batter(Player):
    """타자의 성적 데이터를 관리하고 세부 스탯을 계산하는 클래스입니다."""

    def __init__(self, name: str, team: str):
        """부모 클래스의 생성자를 호출하고 타자 고유 속성을 초기화합니다."""
        super().__init__(name, team)
        self.at_bats = 0  # 타수
        self.hits = 0     # 안타
        self.walks = 0    # 볼넷

    def record_at_bat(self, hits: int, walks: int, at_bats: int) -> None:
        """경기 후 타격 기록을 누적합니다.

        :param hits: 기록한 안타 수
        :param walks: 기록한 볼넷 수
        :param at_bats: 기록한 타수
        """
        if hits < 0 or walks < 0 or at_bats < 0:
            raise ValueError("기록 데이터는 음수일 수 없습니다.")
        if hits > at_bats:
            raise ValueError("안타 수가 타수보다 많을 수 없습니다.")

        self.hits += hits
        self.walks += walks
        self.at_bats += at_bats
        self.update_games(1)

    def _calculate_ratio(self, numerator: int, denominator: int) -> float:
        """비율 스탯 계산 시 ZeroDivisionError를 방지하는 비공개 메서드입니다.

        :param numerator: 분자
        :param denominator: 분모
        :return: 계산된 비율 또는 0.0
        """
        if denominator == 0:
            return 0.000
        return round(numerator / denominator, 3)

    @property
    def batting_average(self) -> float:
        """타자의 타율(AVG)을 계산하여 반환합니다.

        >>> batter = Batter("정여진", "동행")
        >>> batter.record_at_bat(hits=3, walks=1, at_bats=10)
        >>> batter.batting_average
        0.3
        """
        return self._calculate_ratio(self.hits, self.at_bats)


class Pitcher(Player):
    """투수의 성적 데이터를 관리하고 세부 스탯을 계산하는 클래스입니다."""

    def __init__(self, name: str, team: str):
        """부모 클래스의 생성자를 호출하고 투수 고유 속성을 초기화합니다."""
        super().__init__(name, team)
        self.innings_pitched = 0.0  # 던진 이닝 수
        self.earned_runs = 0       # 자책점

    def record_pitch(self, innings: float, earned_runs: int) -> None:
        """경기 후 투구 기록을 누적합니다.

        :param innings: 소화한 이닝 수
        :param earned_runs: 허용한 자책점
        """
        if innings < 0 or earned_runs < 0:
            raise ValueError("기록 데이터는 음수일 수 없습니다.")

        self.innings_pitched += innings
        self.earned_runs += earned_runs
        self.update_games(1)

    def _calculate_ratio(self, numerator: float, denominator: float) -> float:
        """비율 스탯 계산 시 ZeroDivisionError를 방지하는 비공개 메서드입니다."""
        if denominator == 0:
            return 0.00
        return round(numerator / denominator, 2)

    @property
    def earned_run_average(self) -> float:
        """투수의 방어율(ERA)을 계산하여 반환합니다. (9이닝 기준)"""
        return self._calculate_ratio(self.earned_runs*9, self.innings_pitched)
