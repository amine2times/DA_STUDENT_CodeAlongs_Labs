#!/usr/bin/env python3
"""Lab: Solo Class Design Rep
GitBook Quest 1.8: Meet the Objects

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 solo-class-design-practice_STUDENT.py
    Or make it executable once:
        chmod +x solo-class-design-practice_STUDENT.py
    and from then on run it directly:
        ./solo-class-design-practice_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (LiveLabOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

SUBMIT
    Commit this file (you may rename it solo-class-design-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Read the Stakeholder Need =====
# A new stakeholder need. Not the board-game or office-supply domain from
# lecture, and not one of the project's own 4 scenarios.

# Your answer:
#
#

# ===== Step 2: Decide Your Attributes, Each With a Reason From the Scenario =====

# Your answer:
#
#

# ===== Step 3: Write __init__ and a Method, From Scratch =====
# There is no single correct design here. Your class name, your attribute
# names and your method can all differ from everyone else's and still be
# right. The test is whether each one traces back to the stakeholder
# paragraph.
import json
DATA_FILE = ("/Users/amineamine/Documents/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/tools.json")
tools_list = []
with open(DATA_FILE, "r") as file:
    tools_list = json.load(file) 
# TODO: Write __init__ and a Method, From Scratch


class checkedAmount:
    def __init__(self, tool_name):
        self.tool_name = tool_name
        self.total_amount = 0
        self.borrowed_amount = 0
        self.needs_inspection_amount = 0
        self.amount_avail = 0
        for record in tools_list:
            if record["tool_name"] == self.tool_name:
                print(record)
                self.total_amount += 1
                if record["borrowed"] == True:
                    self.borrowed_amount += 1
                if record["inspected"] == False:
                    self.needs_inspection_amount += 1
                if record["borrowed"] == True or record["inspected"] == False:
                    self.amount_avail += 1



        

 


# ===== Step 4: Instantiate 2+ Objects, Confirm Independent Storage =====
# The same proof Day 13's lecture asked for, now on a class you designed
# yourself. Predict what each print() will show before you run it.

# TODO: Instantiate 2+ Objects, Confirm Independent Storage
drill = checkedAmount("Claw Hammer")
print(drill.total_amount)
print(drill.borrowed_amount)
print(drill.needs_inspection_amount)
print(drill.amount_avail)



drill = checkedAmount("Pipe Wrench")
print(drill.total_amount)
print(drill.borrowed_amount)
print(drill.needs_inspection_amount)
print(drill.amount_avail)
# ===== Step 5: Justify Your Design Choice in 2-3 Sentences =====

# Your answer:
#
#

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Come ready to show your class and defend it. Specifically:
# - The attribute list you chose, and for each one, the phrase in the
#   coordinator's request it came from. If you can't point at a phrase for
#   an attribute, say so - that's a real finding, not a failure.
# - One attribute you considered and rejected, and why. - Your method: what
#   question does it answer, and why would the coordinator reach for it
#   first?
# - Anything you got stuck on. Designing from a paragraph with nobody to
#   check against is genuinely hard, and naming where it was hard is worth
#   more to the room than a tidy answer.
#
# Expect to be asked "why that attribute and not another?" - there is no
# single right list here, so the reasoning IS the answer.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#
