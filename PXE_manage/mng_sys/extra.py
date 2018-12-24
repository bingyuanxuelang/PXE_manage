import os
def display(programs):
    display_list = []
    for program in programs:
        display_list.append(program.title)
        children = program.chaildren.all()
        if len(children) >0:
            display_list.append(display_list(program.chaildren.all()))
    return display_list




# def make_file(dir,slug):
