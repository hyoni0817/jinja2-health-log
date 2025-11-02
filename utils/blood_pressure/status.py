from consts.blood_pressure.ranges import BLOOD_PRESSURE_RANGES
from consts.blood_pressure.status import (
    BLOOD_PRESSURE_STATUS_LABELS,
    BLOOD_PRESSURE_STATUS_PRIORITY,
)


# 혈압 상태 라벨 반환
def get_blood_pressure_status_label(status):
    return BLOOD_PRESSURE_STATUS_LABELS[status]


def get_systolic_status(systolic):
    DEFAULT = BLOOD_PRESSURE_RANGES["DEFAULT"]

    if systolic <= DEFAULT["LOW"]["SYSTOLIC"]["MAX"]:
        return "low"
    if systolic <= DEFAULT["NORMAL"]["SYSTOLIC"]["MAX"]:
        return "normal"
    if systolic <= DEFAULT["BORDERLINE"]["SYSTOLIC"]["MAX"]:
        return "borderline"
    if systolic <= DEFAULT["HIGH_STAGE_1"]["SYSTOLIC"]["MAX"]:
        return "high_stage_1"
    if systolic <= DEFAULT["HIGH_STAGE_2"]["SYSTOLIC"]["MAX"]:
        return "high_stage_2"
    return "high_risk"


def get_diastolic_status(diastolic):
    DEFAULT = BLOOD_PRESSURE_RANGES["DEFAULT"]

    if diastolic <= DEFAULT["LOW"]["DIASTOLIC"]["MAX"]:
        return "low"
    if diastolic <= DEFAULT["NORMAL"]["DIASTOLIC"]["MAX"]:
        return "normal"
    if diastolic <= DEFAULT["BORDERLINE"]["DIASTOLIC"]["MAX"]:
        return "borderline"
    if diastolic <= DEFAULT["HIGH_STAGE_1"]["DIASTOLIC"]["MAX"]:
        return "high_stage_1"
    if diastolic <= DEFAULT["HIGH_STAGE_2"]["DIASTOLIC"]["MAX"]:
        return "high_stage_2"
    return "high_risk"


def is_physiologically_valid(systolic, diastolic):
    # 기본 범위 검증
    if systolic <= 0 or diastolic <= 0 or systolic > 1000 or diastolic > 1000:
        return False

    # 맥압(pulse pressure) 검증
    pulse_pressure = systolic - diastolic

    # 수축기는 이완기보다 최소 20mmHg 이상 높아야 함 (의학적 최소 기준)
    if pulse_pressure < 20:
        return False

    # 맥압이 너무 큰 경우도 비현실적 (정상 맥압: 30-60mmHg, 70mmHg 초과시 비정상)
    if pulse_pressure > 80:
        return False

    # 극단적인 조합 검증 (의학적으로 비현실적)
    systolic_status = get_systolic_status(systolic)
    diastolic_status = get_diastolic_status(diastolic)

    # 저혈압 수축기 + 고혈압 이완기 조합은 비현실적
    if systolic_status == "LOW" and (
        diastolic_status == "HIGH_STAGE_1"
        or diastolic_status == "HIGH_STAGE_2"
        or diastolic_status == "HIGH_RISK"
    ):
        return False

    # 정상 수축기 + 극도로 낮은 이완기 조합 검증 (Isolated Diastolic Hypotension)
    # 의학 문헌: 수축기 ≥100, 이완기 <60 조합이 심장질환 위험 증가
    if systolic >= 100 and diastolic < 60:
        return False

    return True


def get_blood_pressure_status(systolic_bp, diastolic_bp):
    if not is_physiologically_valid(systolic_bp, diastolic_bp):
        return "recheck"

    systolic_status = get_systolic_status(systolic_bp)
    diastolic_status = get_diastolic_status(diastolic_bp)

    # 더 높은 위험도의 상태를 반환 (의학적 기준)
    return (
        systolic_status
        if BLOOD_PRESSURE_STATUS_PRIORITY[systolic_status]
        >= BLOOD_PRESSURE_STATUS_PRIORITY[diastolic_status]
        else diastolic_status
    )
