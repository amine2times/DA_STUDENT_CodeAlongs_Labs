#!/usr/bin/env python3
"""Looks Right. Is It?: see DataChallengeOverview&Steps.md for the steps."""

DATA_FILE = "/Users/amineamine/Documents/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/timesheet_hours.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()


# ===== Day 1 =====

# Step 1: Follow the TypeError in `weekly_hours()` Back to Its Cause
# TODO: run the file as given and read the traceback from the bottom up
# TODO: add print(repr(hours)) as the first line of add_hours(); run again
# TODO: find that printed value in the CSV
# TODO: fix the line that reads the wrong column to read the hours column
# TODO: wrap that value in int() so add_hours() adds a number
# TODO: delete the print(repr(hours)) line once Rosa's total is right
def add_hours(total, hours):
    return total + hours


def weekly_hours(lines, emp_id):
    total = 0
    for row in lines[1:]:
        parts = row.split(",")
        if parts[0] == emp_id:
            total = add_hours(total, int(parts[3]))
    return total


print("Rosa Alvarez, weekly hours:", weekly_hours(lines, "E101"))






# Step 1, answer 1:
# Rosa worked 40 hours: 8 + 8 + 8 + 8 + 8 = 40.

# Step 1, answer 2:
# - The last traceback line tells me the exception type and error message.
# - Each block above it shows the function call and line that led to it.
# - I read the traceback from the bottom upward to trace the bad value back.
# I used the Python documentation about Errors and Exceptions.

# Step 1, answer 3:
# The traceback ended in add_hours() at the line that adds total + hours.
# The actual bug was in weekly_hours(): it read parts[2], the day value
# like "Mon", instead of the hours column, parts[3], converted to int.

# Step 2: Trace the ZeroDivisionError Back to the Hand-Typed Staff List
# TODO: run the file as given; note the last ID that printed
# TODO: compare every ID in `staff` with the IDs in the CSV
# TODO: replace the hand-typed `staff` list with an empty list
# TODO: loop over lines[1:]; append each row's employee ID to `staff` once
# TODO: print "employees in the file:" and len(staff)
def days_worked(lines, emp_id):
    days = 0
    for row in lines[1:]:
        if row.split(",")[0] == emp_id:
            days = days + 1
    return days



staff = []
for each in lines[1:]:
    emp_id = each.split(",")[0]
    if emp_id not in staff:
        staff.append(emp_id)
print(staff)
for emp_id in staff:
    hours = weekly_hours(lines, emp_id)
    days = days_worked(lines, emp_id)
    print(emp_id, "| hours:", hours, "| days:", days,
          "| average per day:", hours / days)

# Step 2, answer 1:
# There are 5 employees in the CSV.

# Step 2, answer 2:
# Five employee lines printed before the crash. It stopped on E106.

# Step 2, answer 3:
# The bug was above the division line: the hand-typed staff list included
# E106, which is not in the CSV, so days_worked returned 0.


# ===== Day 2 =====

# Step 3: Find Why Four of the Five Weekly Hour Totals Are Wrong
# TODO: add up Rosa's (E101) *40* and Mei's (E103) *32* hours by hand first
# TODO: print("starting", emp, "total is", total) first in the outer loop
# TODO: move the line that sets `total` inside the outer loop
# TODO: delete the "starting" print once all five totals are right
records = []
for row in lines[1:]:
    emp_id, name, day, hours, rate = row.split(",")
    records.append({"id": emp_id, "name": name, "day": day,
                    "hours": int(hours), "rate": float(rate)})


employee_ids = []
for r in records:
    if r["id"] not in employee_ids:
        employee_ids.append(r["id"])


for emp in employee_ids:
    total = 0
    name = ""
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            total = total + r["hours"]
    print(emp, name, "| weekly hours:", total)


# Step 3, answer 1:
# Rosa worked 40 hours and Mei worked 32 hours.

# Step 3, answer 2:
# Before the fix, total started at 0 for E101, then 40 for E102, 86 for
# E103, 118 for E104, and 156 for E105. The line total = 0 was outside
# the outer loop, so it ran only once instead of once per employee.

# Step 3, answer 3:
# Rosa's number was right because she was counted first, when total was 0.
# Priya's total became the whole staff's weekly hours because every earlier
# employee's hours were still stored in total.


# Step 4: Fix Two Overtime Bugs That Overpay the Firm by $1,810 a Week
# TODO: work out Rosa's *960*, Darnell's *1543.50* and Mei's *896* pay by hand first
# TODO: fix weekly_pay() so it follows the handbook rule word for word
# TODO: fix the other line that compares `total` against 40 the same way
def weekly_pay(hours, rate):
    if hours > 40:
        ot_hours = hours - 40
        ot_rate = rate * 1.5
        ot_pay = ot_hours * ot_rate
        reg_pay = 40 * rate
        return reg_pay + ot_pay
    return hours * rate


owed_overtime = 0
payroll = 0.0
for emp in employee_ids:
    total = 0
    name = ""
    rate = 0.0
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            rate = r["rate"]
            total = total + r["hours"]
    if total > 40:
        owed_overtime = owed_overtime + 1
    pay = weekly_pay(total, rate)
    payroll = payroll + pay
    print(f"{name:16} {total:3} hrs  ${pay:>9,.2f}")

print("employees owed overtime:", owed_overtime)
print(f"TOTAL PAYROLL: ${payroll:,.2f}")


# Step 4, answer 1:
# Rosa: 40 * $24.00 = $960.00.
# Darnell: (40 * $31.50) + (6 * $47.25) = $1,543.50.
# Mei: 32 * $28.00 = $896.00.

# Step 4, answer 2:
# The first bug was in weekly_pay(): it paid all hours at 1.5 times the
# rate for an overtime week. I changed it so only hours over 40 get 1.5x,
# while the first 40 hours stay at the regular rate.
# The second bug was the overtime counter using >= 40. I changed it to > 40.

# Step 4, answer 3:
# Only Rosa's exactly-40-hour week catches the >= versus > bug. Both
# conditions behave the same for weeks below 40 or above 40 hours, but
# they differ when the total is exactly 40.