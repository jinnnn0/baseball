"""야구 데이터 분석 패키지의 핵심 기본 클래스를 정의하는 모듈입니다."""


class Player:
    """모든 야구 선수의 공통 정보를 관리하는 부모 클래스입니다."""

    def __init__(self, name: str, team: str):
        """선수 객체를 초기화합니다.

        :param name: 선수의 이름
        :param team: 소속 팀 이름
        """
        self.name = name
        self.team = team
        self.games_played = 0

    def update_games(self, count: int = 1) -> None:
        """선수의 출장 경기 수를 업데이트합니다.

        :param count: 추가할 경기 수 (기본값 1)
        """
        if count < 0:
            raise ValueError("경기 수는 음수가 될 수 없습니다.")
        self.games_played += count

    def get_profile(self) -> str:
        """선수의 기본 프로필 정보를 문자열로 반환합니다.

        :return: 선수 프로필 문자열
        """
        return f"[{self.team}] {self.name} (출장: {self.games_played}경기)"
