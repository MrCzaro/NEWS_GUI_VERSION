import PySimpleGUI as sg
from fpdf import FPDF
from datetime import datetime
from pathlib import Path


def about():
    """Returns info about NEWS"""
    info = (
        "This National Early Warning Score (NEWS) calculator\n"
        + "evaluates physiological parameters to check the severity\n"
        + "and decline of illness in patients.\n"
        + "Discover more about the early warning systems and the score\n"
        + "interpretation below the form.\n"
        + "Please fill in all requires pool. The program will promt you\n"
        + "to do so before you will be able to check and save record as a pdf file."
    )
    return info


def validate_path(file_path: str) -> bool:
    if file_path and Path(file_path).exists():
        return True
    else:
        return False


def respiratory_rate(rate: int):
    """
    Function takes one argument int (raspiratory rate) and according to NEWS
    gives score depending on input.
    Returns int (score) or string if input is invalid.
    """
    try:
        rate = int(rate)
        if rate >= 0 and rate <= 8:
            return 3
        elif rate >= 9 and rate <= 11:
            return 1
        elif rate >= 12 and rate <= 20:
            return 0
        elif rate >= 21 and rate <= 24:
            return 2
        elif rate > 24:
            return 3
        else:
            return "Invalid input!, please use positive numbers."
    except:
        return "Please enter patient's raspiratory rate. Please use positive number."


def oxygen_saturation(saturation: int, oxygen: str, state: str) -> int:
    """
    Function takses three arguments:
    * saturation - int (patient's saturation level),
    * oxygen - str (yes/no - if patient requires oxygen),
    * state - str (yest/no - if the patient is in AECOPD)
    According to NEWS gives score depending on input.
    Returns int (score).
    """
    # If patient is in AECOPD state:
    try:
        saturation = int(saturation)
        if state == "yes":
            if saturation >= 0 and saturation <= 83:
                return 3
            elif saturation >= 84 and saturation <= 85:
                return 2
            elif saturation >= 86 and saturation <= 87:
                return 1
            elif (saturation >= 88 and saturation <= 92) or (
                saturation >= 93 and saturation <= 100 and oxygen == "no"
            ):
                return 0
            elif oxygen == "yes":
                if saturation in [93, 94]:
                    return 1
                elif saturation in [95, 96]:
                    return 2
                elif saturation >= 97 and saturation <= 100:
                    return 3
            else:
                return "Invalid input!"
        # If the patient is not in AECOPD state:
        elif state == "no":
            if saturation >= 0 and saturation <= 91:
                return 3
            elif saturation in [92, 93]:
                return 2
            elif saturation in [94, 95]:
                return 1
            elif saturation >= 96 and saturation <= 100:
                return 0
            else:
                return "Invalid input!"
        else:
            return "Invalid input!"
    except:
        return "Invalid input!"


def oxygen_supplementation(oxygen: str) -> int:
    """
    Function takes string ("YES" or "NO") and according to NEWS
    gives score depending on input..
    Returns int (score).
    """
    oxygen = oxygen.lower()
    if oxygen == "yes":
        return 2
    elif oxygen == "no":
        return 0
    # Condition for testing wrong input:
    else:
        return "Invalid input!"


def temperature(temp: float) -> int:
    """
    Function takes one argument float (temperature) and according to NEWS
    gives score depending on input.
    Returns int (score).
    """
    try:
        temp = float(temp)
        if temp > 0 and temp <= 35.0:
            return 3
        elif temp >= 35.1 and temp <= 36.0:
            return 1
        elif temp >= 36.1 and temp <= 38.0:
            return 0
        elif temp >= 38.1 and temp <= 39.0:
            return 1
        elif temp >= 39.1:
            return 2
        # Condition for testing wrong input:
        else:
            return "Invalid input!"
    except:
        return "Invalid input!"


def systolic_blood_pressure(systolic: int) -> int:
    """
    Function takes one argument int(systolic blood pressure) and according to NEWS
    gives score depending on input.
    Return int (score).
    """
    try:
        systolic = int(systolic)
        if systolic >= 0 and systolic <= 90:
            return 3
        elif systolic >= 91 and systolic <= 100:
            return 2
        elif systolic >= 101 and systolic <= 110:
            return 1
        elif systolic >= 111 and systolic <= 219:
            return 0
        elif systolic >= 220:
            return 3
        # Condition for testing wrong input
        else:
            return "Invalid input!"
    except:
        return "Invalid input!"


def heart_rate(rate: int) -> int:
    """
    Function takes one argument int (heart rate) and according to NEWS
    gives score depending on input.
    Returns int (score).
    """
    try:
        rate = int(rate)
        if rate > 0 and rate <= 40:
            return 3
        elif rate >= 40 and rate <= 50:
            return 1
        elif rate >= 51 and rate <= 90:
            return 0
        elif rate >= 91 and rate <= 110:
            return 1
        elif rate >= 111 and rate <= 130:
            return 2
        elif rate > 131:
            return 3
        # Condition for testing wrong input:
        else:
            return "Invalid input!"
    except:
        return "Invalid input!"


def level_of_consciousness(level: str) -> int:
    """
    Function takes one argument string(patient's level of consciousness) and according to NEWS
    gives score depending on input.
    Returns int (score).
    """
    level = level.lower()
    if level == "awake":
        return 0
    elif level in ["verbal", "pain", "unresponsive"]:
        return 3
    # Condition for testing wrong input:
    else:
        return "Invalid input!"


def score_interpretation(score: int) -> str:
    """
    Function takes positive number (NEWS score) and depending on result
    returns string with description according to the NEWS criteria.
    """
    try:
        score = int(score)
        if score >= 0 and score <= 4:
            result = (
                f"National Early Warning Score (NEWS) = {score}.\n"
                + "Interpretation: This is a low score that suggests clinical monitoring should be continued\n"
                + "and the medical professional, usually a registered nurse will decide further if clinical\n"
                + "care needs to be upadted.\n"
                + "Note: This tool should NOT be considered as a substitute for any professional medical service,\n"
                + "NOR as a substitute for clinical judgement."
            )
            return result
        elif score in [5, 6]:
            result = (
                f"National Early Warning Score (NEWS) = {score}.\n"
                + "Interpretation: This is a medium score that suggests the patient should be reviewed by a medical\n"
                + "specialist with competencies in acute illness, even with the possibility of referring the patient\n"
                + "to the critical care unit at the end of the assessment.\n"
                + "Note: This tool should NOT be considered as a substitute for any professional medical service,\n"
                + "NOR as a substitute for clinical judgement."
            )
            return result
        elif score >= 7 and score <= 20:
            result = (
                f"National Early Warning Score (NEWS) = {score}.\n"
                + "Interpretation: This is a high score (red score) that is indicative of urgent critical care need and\n"
                + "the patient should be transferred to the appropriate specialized department for further care.\n"
                + "Note: This tool should NOT be considered as a substitute for any professional medical service,\n"
                + "NOR as a substitute for clinical judgement."
            )
            return result
        else:
            return "Invalid input!"
    except:
        return "Invalid input!"


def main():

    title = "National Early Warning Score Calculator"
    menu_layout = [["FILE", ["New", "Save", "---", "About", "---", "Exit"]]]

    layout = [
        [sg.Menu(menu_layout)],
        [sg.Text(title)],
        [sg.Text("First name: ", size=(10, 0)), sg.Input(key="_name_", size=(25, 0))],
        [
            sg.Text("Last name: ", size=(10, 0)),
            sg.Input(key="_last_name_", size=(25, 0)),
        ],
        [sg.Text("Patient ID: ", size=(10, 0)), sg.Input(key="_id_", size=(25, 0))],
        [sg.Text("Oxygen supplementation: ")],
        [sg.Radio("YES", "oxygen"), sg.Radio("NO", "oxygen", default=True)],
        [sg.Text("Is the patient is in acute exacerbations of chronic")],
        [sg.Text("obstructive pulomanry disease state:")],
        [sg.Radio("YES", "acute"), sg.Radio("NO", "acute", default=True)],
        [
            sg.Text("Oxygen saturation level: ", size=(20, 0)),
            sg.Input(key="_sat_", size=(4, 0)),
        ],
        [
            sg.Text("Respiratory Rate: ", size=(20, 0)),
            sg.Input(key="_rr_", size=(4, 0)),
        ],
        [sg.Text("Heart Rate: ", size=(20, 0)), sg.Input(key="_hr_", size=(4, 0))],
        [
            sg.Text("Body temperature: ", size=(20, 0)),
            sg.Input(key="_temp_", size=(4, 0)),
        ],
        [
            sg.Text("Blood Pressure: ", size=(20, 0)),
            sg.Input(key="_systolic_", size=(4, 0)),
            sg.Text("/"),
            sg.Input(key="_diastolic_", size=(4, 0)),
        ],
        [sg.Text("Level of consciousness: ")],
        [
            sg.Radio("Awake", "loc", default=True),
            sg.Radio("Responds to verbal stimulus", "loc"),
        ],
        [sg.Radio("Responds to pain simulus", "loc"), sg.Radio("Unresponsive", "loc")],
        [sg.Input(key="_save_", size=(30, 0)), sg.FolderBrowse()],
        [sg.Button("Check"), sg.Button("Save"), sg.Button("Clear")],
    ]
    window = sg.Window(title, layout, margins=(0, 0), size=(360, 500))

    while True:
        event, values = window.read()
        if event in ("Exit", sg.WINDOW_CLOSED):
            break
        if event in ["New", "Clear"]:
            clear_key = [
                "_name_",
                "_last_name_",
                "_id_",
                "_rr_",
                "_sat_",
                "_hr_",
                "_temp_",
                "_systolic_",
                "_diastolic_",
                "_save_",
            ]
            for key in clear_key:
                window[key]("")
            window[2](True)
            window[4](True)
            window[5](True)
            #sg.popup("Cleared!", no_titlebar=True)
        if event == "About":
            sg.popup(about(), no_titlebar=True)
        if event == "Check":
            score = 0
            if values[1] == True:
                oxygen = "yes"
            else:
                oxygen = "no"
            score += oxygen_supplementation(oxygen)
            if values[3] == True:
                state = "yes"
            else:
                state = "no"
            if values[5] == True:
                level = "awake"
            elif values[6] == True:
                level = "verbal"
            elif values[7] == True:
                level = "pain"
            else:
                level = "unresponsive"
            score += level_of_consciousness(level)
            first_name = values["_name_"]
            last_name = values["_last_name_"]
            patient_id = values["_id_"]
            respi_rate = values["_rr_"]
            saturation = values["_sat_"]
            heart_r = values["_hr_"]
            body_temp = values["_temp_"]
            bp_systolic = values["_systolic_"]
            bp_diastolic = values["_diastolic_"]
            if len(first_name) < 1:
                sg.popup("Please enter patient's first name.", no_titlebar=True)
            elif first_name.isalpha() == False:
                sg.popup("Please enter correct patient's first name.", no_titlebar=True)
            else:
                if len(last_name) < 1:
                    sg.popup("Please enter patient's last name.", no_titlebar=True)
                elif last_name.isalpha() == False:
                    sg.popup(
                        "Please enter correct patient's last name.", no_titlebar=True
                    )
                else:
                    if len(patient_id) < 1:
                        sg.popup("Please enter patient's id number.", no_titlebar=True)
                    else:
                        try:
                            patient_id = int(patient_id)
                        except:
                            sg.popup(
                                "Please enter patient's id number, please use positive numbers.",
                                no_titlebar=True,
                            )
                    if len(respi_rate) < 1:
                        sg.popup(
                            "Please enter patient's respiratory rate.", no_titlebar=True
                        )
                    else:
                        try:
                            if int(respi_rate) < 0:
                                sg.popup(
                                    "Please enter patient's respiratory rate, please use positive numbers.",
                                    no_titlebar=True,
                                )
                            else:
                                score += respiratory_rate(respi_rate)
                        except:
                            sg.popup(
                                "Please enter patient's respiratory rate, please use positive numbers.",
                                no_titlebar=True,
                            )

                        if len(saturation) < 1:
                            sg.popup(
                                "Please enter patient's oxygen saturation.",
                                no_titlebar=True,
                            )
                        else:
                            try:
                                if int(saturation) < 0:
                                    sg.popup(
                                        "Please enter patient's oxygen saturation level, please use positive numbers.",
                                        no_titlebar=True,
                                    )
                                else:
                                    score += oxygen_saturation(
                                        saturation, oxygen, state
                                    )
                            except:
                                sg.popup(
                                    "Please enter patient's oxygen saturation  level.",
                                    no_titlebar=True,
                                )
                            if len(heart_r) < 1:
                                sg.popup(
                                    "Please enter patient's heart rate.",
                                    no_titlebar=True,
                                )
                            else:
                                try:
                                    if int(heart_r) < 0:
                                        sg.popup(
                                            "Please enter patient's heart rate, please use positive numbers.",
                                            no_titlebar=True,
                                        )
                                    else:
                                        score += heart_rate(heart_r)
                                except:
                                    sg.popup(
                                        "Please enter patient's heart rate.",
                                        no_titlebar=True,
                                    )
                                if len(body_temp) < 1:
                                    sg.popup(
                                        "Please enter patient's body temperature.",
                                        no_titlebar=True,
                                    )
                                else:
                                    try:
                                        if float(body_temp) < 0:
                                            sg.popup(
                                                "Please enter patient's body temperature, please use positive numbers.",
                                                no_titlebar=True,
                                            )
                                        else:
                                            score += temperature(body_temp)
                                    except:
                                        sg.popup(
                                            "Please enter patient's body temperature.",
                                            no_titlebar=True,
                                        )
                                    if len(bp_systolic) < 1 and len(bp_diastolic) < 1:
                                        sg.popup(
                                            "Please enter patient's blood pressure.",
                                            no_titlebar=True,
                                        )
                                    else:
                                        try:
                                            if int(bp_systolic) < 0:
                                                sg.popup(
                                                    "Please enter patient's blood pressure, please use positive numbers.",
                                                    no_titlebar=True,
                                                )
                                            else:
                                                score += systolic_blood_pressure(
                                                    bp_systolic
                                                )
                                                interpretation = score_interpretation(
                                                    score
                                                )
                                                sg.popup(
                                                    interpretation, no_titlebar=True
                                                )
                                                check = True
                                        except:
                                            sg.popup(
                                                "Please enter patient's blood pressure.",
                                                no_titlebar=True,
                                            )
        if event == "Save":
            if validate_path(values["_save_"]) == True:
                try:
                    if check == True:
                        # Create and save result in pdf file:
                        pdf = FPDF()
                        pdf.add_page()
                        pdf.set_auto_page_break(True)
                        # Title:
                        pdf.set_font("Arial", "B", 20)
                        pdf.text(20, 20, "NATIONAL EARLY WARNING SCORE CHART")
                        # Patient's personal data:
                        pdf.set_font("Arial", "", 12)
                        pdf.text(20, 40, f"First Name: {first_name.upper()}")
                        pdf.text(20, 45, f"Last Name: {last_name.upper()}")
                        pdf.text(20, 50, f"Patient's Id number: {str(patient_id)}")
                        # Header:
                        pdf.set_font("Arial", "B", 14)
                        pdf.text(20, 80, "National Early Warning Score:")
                        # Stats:
                        pdf.set_font("Arial", "", 12)
                        pdf.text(
                            20,
                            100,
                            f"Respiratory Rate: {str(respi_rate)} bpm. ------ {str(respiratory_rate(respi_rate))} points.",
                        )
                        pdf.text(
                            20,
                            110,
                            f"Oxygen Saturation: {str(saturation)} %. ------ {str(oxygen_saturation(saturation, oxygen, state))} points.",
                        )
                        pdf.text(
                            20,
                            120,
                            f"Oxygen Supplementation : {oxygen.title()}. ------ {str(oxygen_supplementation(oxygen))} points.",
                        )
                        pdf.text(
                            20,
                            130,
                            f"Temperature: {str(body_temp)} C. ------ {str(temperature(body_temp))} points.",
                        )
                        pdf.text(
                            20,
                            140,
                            f"Blood Pressure: {str(bp_systolic)} / {str(bp_diastolic)}. ------ {str(systolic_blood_pressure(bp_systolic))} points.",
                        )
                        pdf.text(
                            20,
                            150,
                            f"Heart Rate: {str(heart_r)} bpm. ------ {str(heart_rate(heart_r))} points.",
                        )
                        pdf.text(
                            20,
                            160,
                            f"AVPU Score: {level}. ------ {str(level_of_consciousness(level))} points.",
                        )
                        # Total amount of point:
                        pdf.text(20, 170, f"Total Score: {str(score)} points.")
                        # Display Score Interpretation :

                        pdf.set_font("Arial", "B", 14)
                        pdf.text(80, 200, f"Score Interpretation:")
                        pdf.set_font("Arial", "", 12)
                        pdf.text(
                            10,
                            220,
                            f"National Early Warning Score (NEWS) ={str(score)}.",
                        )
                        if score >= 0 and score <= 4:
                            pdf.text(
                                10,
                                225,
                                "Interpretation: This is a low score that suggests clinical monitoring should be continued and the medical",
                            )
                            pdf.text(
                                10,
                                230,
                                "professional, usually a registered nurse will decide further if clinical care needs to be updated.",
                            )
                            pdf.text(
                                10,
                                235,
                                "Note: This tool should NOT be considered as a substitute for any prosefssional medical service,",
                            )
                            pdf.text(
                                10, 240, "NOR as a substitute for clinical judgement."
                            )
                        elif score in [5, 6]:
                            pdf.text(
                                10,
                                225,
                                "Interpretation: This is a medium score that suggests the patient should be reviewed by a medical",
                            )
                            pdf.text(
                                10,
                                230,
                                "specialist with competencies in acute illness, even with the possibility of referring the patient",
                            )
                            pdf.text(
                                10,
                                235,
                                "to the critical care unit at the end of the assessment.",
                            )
                            pdf.text(
                                10,
                                240,
                                "Note: This tool should NOT be considered as a substitute for any professional medical service,",
                            )
                            pdf.text(
                                10, 245, "NOR as a substitute for clinical judgement"
                            )
                        elif score >= 7 and score <= 20:
                            pdf.text(
                                10,
                                225,
                                "Interpretation: This is a high score (red score) that is indicative of urgent critical care need",
                            )
                            pdf.text(
                                10,
                                230,
                                "and the patient should be transferred to the appropriate specialized department for further care.",
                            )
                            pdf.text(
                                10,
                                235,
                                "Note: This tool should NOT be considered as a substitute for any professional medical service,",
                            )
                            pdf.text(
                                10, 240, "NOR as a substitute for clinical judgement."
                            )
                        # Current date:
                        today = datetime.now()
                        time = today.strftime("%H:%M:%S")
                        day = today.strftime("%Y-%m-%d")
                        # Display current date on pdf file:
                        pdf.text(140, 290, f"Created on: {day}, {time}")
                        pdf.output(
                            Path(values["_save_"])
                            / f"{first_name}_{last_name}_{day}_{time}.pdf"
                        )
                        sg.popup("Saved!", no_titlebar=True)
                    else:
                        sg.popup(
                            "Please fullfill all pools! and press Check. Then try again.",
                            no_titlebar=True,
                        )

                except:
                    sg.popup(
                        "Please fulfill all the pools and press Check. Then try again.",
                        no_titlebar=True,
                    )
            else:
                sg.popup("Incorrect file path!", no_titlebar=True)
    window.close()


if __name__ == "__main__":
    main()
