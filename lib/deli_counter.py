# import ipdb
def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently:"
        for i, name in enumerate(katz_deli, start=1):
            line_status += f" {i}. {name}"
            if i != len(katz_deli) - 1:
                line_status += " "
        line_status += "\n"  # Ensure the output ends with a newline
        print(line_status)


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"The line is currently: {position}. {name}\n")
    
def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        next_person = katz_deli.pop(0)
    print(f"Now serving {next_person}!")

katz_deli = []
take_a_number(katz_deli,"Logan")
take_a_number(katz_deli,"Avi")
take_a_number(katz_deli,"Spencer")
now_serving(katz_deli)
line(katz_deli)
take_a_number(katz_deli,"Dave")
line(katz_deli)
now_serving(katz_deli)
line(katz_deli)
