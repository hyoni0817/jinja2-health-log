from consts.blood_sugar.ranges import BLOOD_SUGAR_RANGES
from consts.blood_sugar.status import BLOOD_SUGAR_STATUS_STYLES


# 혈당 상태 라벨 반환
def get_blood_sugar_status_label(status):
    return BLOOD_SUGAR_STATUS_STYLES[status]


# 혈당 수치에 따른 상태 판정
def get_blood_sugar_status(value, measurement_timing, post_meal_time):
    BEFORE_MEAL_TIME = BLOOD_SUGAR_RANGES["BEFORE_MEAL_TIME"]
    AFTER_MEAL_TIME = BLOOD_SUGAR_RANGES["AFTER_MEAL_TIME"]
    is_before_measurement_timing = "BEFORE" in measurement_timing
    is_fasting = measurement_timing == "FASTING"

    if is_before_measurement_timing:
        # 식전
        if value <= BEFORE_MEAL_TIME["PRE_MEAL"]["LOW"]["MAX"]:
            return "low"
        if (
            BEFORE_MEAL_TIME["PRE_MEAL"]["NORMAL"]["MIN"] <= value
            and value <= BEFORE_MEAL_TIME["PRE_MEAL"]["NORMAL"]["MAX"]
        ):
            return "normal"
        if (
            BEFORE_MEAL_TIME["PRE_MEAL"]["BORDERLINE"]["MIN"] <= value
            and value <= BEFORE_MEAL_TIME["PRE_MEAL"]["BORDERLINE"]["MAX"]
        ):
            return "borderline"
        if (
            BEFORE_MEAL_TIME["PRE_MEAL"]["HIGH_RISK"]["MIN"] <= value
            and value <= BEFORE_MEAL_TIME["PRE_MEAL"]["HIGH_RISK"]["MAX"]
        ):
            return "high_risk"
    elif is_fasting:
        # 공복
        if value <= BEFORE_MEAL_TIME["FASTING"]["LOW"]["MAX"]:
            return "low"
        if (
            BEFORE_MEAL_TIME["FASTING"]["NORMAL"]["MIN"] <= value
            and value <= BEFORE_MEAL_TIME["FASTING"]["NORMAL"]["MAX"]
        ):
            return "normal"
        if (
            BEFORE_MEAL_TIME["FASTING"]["BORDERLINE"]["MIN"] <= value
            and value <= BEFORE_MEAL_TIME["FASTING"]["BORDERLINE"]["MAX"]
        ):
            return "borderline"
        if (
            BEFORE_MEAL_TIME["FASTING"]["HIGH_RISK"]["MIN"] <= value
            and value <= BEFORE_MEAL_TIME["FASTING"]["HIGH_RISK"]["MAX"]
        ):
            return "high_risk"
    else:
        # 식후
        if value <= AFTER_MEAL_TIME[post_meal_time]["LOW"]["MAX"]:
            return "low"
        if (
            AFTER_MEAL_TIME[post_meal_time]["NORMAL"]["MIN"] <= value
            and value <= AFTER_MEAL_TIME[post_meal_time]["NORMAL"]["MAX"]
        ):
            return "normal"
        if (
            AFTER_MEAL_TIME[post_meal_time]["BORDERLINE"]["MIN"] <= value
            and value <= AFTER_MEAL_TIME[post_meal_time]["BORDERLINE"]["MAX"]
        ):
            return "borderline"
        if (
            AFTER_MEAL_TIME[post_meal_time]["HIGH_RISK"]["MIN"] <= value
            and value <= AFTER_MEAL_TIME[post_meal_time]["HIGH_RISK"]["MAX"]
        ):
            return "high_risk"

    return "recheck"
