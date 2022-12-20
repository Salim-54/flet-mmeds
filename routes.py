import components
import prescription
import thank_you
import delivering


current_step = str

# system_pages = [components.token(),
#                 prescription.prescription(),
#                 thank_you.finish(),
#                 delivering.delivering(),]


def display(step):
    match step:
        case "home":
            return components.token()

        case "prescription":
            return prescription.prescription()

        case "end":
            return thank_you.finish()

        case "delivering":
            return delivering.delivering()

        case _:
            return components.token()
