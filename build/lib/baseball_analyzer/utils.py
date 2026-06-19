def clean_percentage(value: float) -> str:
    """소수점 형태의 타율을 야구 표준 포맷(예: .300)으로 변환합니다."""
    if value is None:
        return ".000"

    # 소수점 3자리까지 고정하여 변환 (예: 0.3 -> '0.300')
    formatted = f"{value:.3f}"

    # 맨 앞의 '0'을 제거하여 반환 (예: '0.300' -> '.300')
    if formatted.startswith("0."):
        return formatted[1:]
    return formatted
