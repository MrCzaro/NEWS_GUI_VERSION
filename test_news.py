from news import (
    respiratory_rate,
    oxygen_saturation,
    oxygen_supplementation,
    temperature,
    systolic_blood_pressure,
    heart_rate,
    level_of_consciousness,
    score_interpretation,
)


def test_respiratory_rate():
    # Test correct input:
    assert respiratory_rate(7) == 3
    assert respiratory_rate(10) == 1
    assert respiratory_rate(19) == 0
    assert respiratory_rate(22) == 2
    assert respiratory_rate(25) == 3
    # Test incorrect input:
    assert respiratory_rate(-10) == "Invalid input!, please use positive numbers."
    assert (
        respiratory_rate(None)
        == "Please enter patient's raspiratory rate. Please use positive number."
    )
    assert (
        respiratory_rate("as")
        == "Please enter patient's raspiratory rate. Please use positive number."
    )


def test_oxygen_saturation():
    # Test correct input:
    assert oxygen_saturation(99, "no", "no") == 0
    assert oxygen_saturation(81, "no", "no") == 3
    assert oxygen_saturation(93, "no", "no") == 2
    assert oxygen_saturation(95, "no", "no") == 1
    assert oxygen_saturation(97, "yes", "yes") == 3
    assert oxygen_saturation(95, "yes", "yes") == 2
    assert oxygen_saturation(93, "yes", "yes") == 1
    assert oxygen_saturation(88, "no", "yes") == 0
    assert oxygen_saturation(95, "no", "yes") == 0
    assert oxygen_saturation(87, "no", "yes") == 1
    assert oxygen_saturation(85, "no", "yes") == 2
    assert oxygen_saturation(80, "no", "yes") == 3
    # Test incorrec input:
    assert oxygen_saturation("", "", "") == "Invalid input!"
    assert oxygen_saturation(-12, "YES", "N") == "Invalid input!"
    assert oxygen_saturation(1000, "y", "NOT") == "Invalid input!"


def test_oxygen_supplementation():
    # Test correct input:
    assert oxygen_supplementation("yes") == 2
    assert oxygen_supplementation("No") == 0
    # Test incorrect input:
    assert oxygen_supplementation(" ") == "Invalid input!"
    assert oxygen_supplementation("123") == "Invalid input!"


def test_temperature():
    # Test correct input:
    assert temperature(33.0) == 3
    assert temperature(35.2) == 1
    assert temperature(38) == 0
    assert temperature(39) == 1
    assert temperature(41) == 2
    assert temperature(44) == 2
    # Test incorrect input:
    assert temperature(-1) == "Invalid input!"


def test_systolic_blood_pressure():
    # Test correct input:
    assert systolic_blood_pressure(77) == 3
    assert systolic_blood_pressure(92) == 2
    assert systolic_blood_pressure(109) == 1
    assert systolic_blood_pressure(210) == 0
    assert systolic_blood_pressure(222) == 3
    # Test incorrect input:
    systolic_blood_pressure(-220) == "Invalid input!"


def test_heart_rate():
    # Test correct input:
    assert heart_rate(33) == 3
    assert heart_rate(45) == 1
    assert heart_rate(88) == 0
    assert heart_rate(100) == 1
    assert heart_rate(112) == 2
    assert heart_rate(133) == 3
    # Test incorrect input:
    assert heart_rate(-1) == "Invalid input!"


def test_level_of_consciousness():
    # Test correct input:
    assert level_of_consciousness("awake") == 0
    assert level_of_consciousness("AwAke") == 0
    assert level_of_consciousness("VERBAL") == 3
    assert level_of_consciousness("pain") == 3
    # Test incorrect input:
    assert level_of_consciousness(" ") == "Invalid input!"
    assert level_of_consciousness("asa21") == "Invalid input!"
    assert level_of_consciousness("123") == "Invalid input!"


def test_score_intepretation():
    # Test correct input:
    assert (
        score_interpretation(2)
        == f"National Early Warning Score (NEWS) = 2.\n"
        + "Interpretation: This is a low score that suggests clinical monitoring should be continued\n"
        + "and the medical professional, usually a registered nurse will decide further if clinical\n"
        + "care needs to be upadted.\n"
        + "Note: This tool should NOT be considered as a substitute for any professional medical service,\n"
        + "NOR as a substitute for clinical judgement."
    )
    assert (
        score_interpretation(5)
        == f"National Early Warning Score (NEWS) = 5.\n"
        + "Interpretation: This is a medium score that suggests the patient should be reviewed by a medical\n"
        + "specialist with competencies in acute illness, even with the possibility of referring the patient\n"
        + "to the critical care unit at the end of the assessment.\n"
        + "Note: This tool should NOT be considered as a substitute for any professional medical service,\n"
        + "NOR as a substitute for clinical judgement."
    )

    assert (
        score_interpretation(17)
        == f"National Early Warning Score (NEWS) = 17.\n"
        + "Interpretation: This is a high score (red score) that is indicative of urgent critical care need and\n"
        + "the patient should be transferred to the appropriate specialized department for further care.\n"
        + "Note: This tool should NOT be considered as a substitute for any professional medical service,\n"
        + "NOR as a substitute for clinical judgement."
    )
    # Test incorrect input:
    assert score_interpretation("asa") == "Invalid input!"
    assert score_interpretation(-1) == "Invalid input!"
    assert score_interpretation(22) == "Invalid input!"
