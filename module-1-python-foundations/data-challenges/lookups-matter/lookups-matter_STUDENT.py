#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "/Users/amineamine/Documents/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "/Users/amineamine/Documents/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    # TODO: assign `comparisons` to 0
    # TODO: loop over `members`; add 1 to `comparisons` for every row
    # TODO: inside the loop, return row, comparisons on a member_id match
    # TODO: after the loop, return None, comparisons
    comparisons = 0
    for member in members:
        comparisons += 1
        if member["member_id"] == member_id:
            return (member, comparisons)
    return (None, comparisons)
    pass


row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1:
# 300


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`
# TODO: open CHECKINS_FILE in a with block as `f`
# TODO: inside it, assign `swipes` to f.read().splitlines()
# TODO: assign `linear_total` and `not_members` to 0
# TODO: loop over `swipes`; call find_linear(members, member_id)
# TODO: print the ID, the name or "NOT A MEMBER", and the comparisons
# TODO: add each count to `linear_total`
# TODO: add 1 to `not_members` for every swipe with no row

with open(CHECKINS_FILE, newline="") as f:
    swipes = f.read().splitlines()

linear_total = 0
not_members = 0
for member in swipes:
    row, comparisons = find_linear(members, member)
    if row is None:
        print(member, "NOT A MEMBER", comparisons)
        not_members += 1
    elif row["member_id"]:
        print(row["member_id"], row["name"], comparisons)
        linear_total += comparisons
        


print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)

# Step 2, answer 1:
# There are 20 swipes. I do notice that I spot a duplicate of M1004.
# Step 2, answer 2:
# M1004: 4, M1012: 12, M1027: 27
# Sum: 43
# A non-member costs 312 comparisons.


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off
# TODO: assign `members_by_id` to an empty dict and `build_steps` to 0
# TODO: loop over `members`; store each row under row["member_id"]
# TODO: add 1 to `build_steps` for every row
# TODO: write find_dict(members_by_id, member_id)
# TODO: make find_dict() return members_by_id.get(member_id), 1

members_by_id = {}
build_steps = 0
for member in members:
    members_by_id[member["member_id"]] = member
    build_steps += 1

def find_dict(members_by_id, member_id):
    return (members_by_id.get(member_id), 1)

print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))

# TODO: assign `linear_running` to 0 and `dict_running` to build_steps
linear_running = 0
dict_running = build_steps
# TODO: assign `pays_off_at` to None and `swipe_number` to 0
pays_off_at = None
swipe_number = 0

for member_id in swipes:
    # TODO: add 1 to `swipe_number`
    swipe_number += 1
    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)
    # TODO: add each search's count to its running total
    linear_running += linear_count
    dict_running += dict_count
    # TODO: print swipe_number, the ID and both running totals
    print(swipe_number, member_id, linear_running, dict_running)
    # TODO: the first time dict_running < linear_running, set `pays_off_at`
    if dict_running < linear_running:
        pays_off_at = swipe_number

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1:
# I predict the dictionary pays off at swipe 6, M1313. After swipe 5,
# linear is 262 and dictionary is 317; after swipe 6, linear is 574
# and dictionary is 318.

# Step 3, answer 2:
# A dictionary keyed on member_id fits the door's job because it looks
# up IDs repeatedly. It has a one-time build cost, then each lookup is
# O(1) average-case. It first pulled ahead at swipe 6.

# Step 3, answer 3:
# A plain list is better for a very short morning with only a few
# swipes. For example, after the first five swipes, linear costs 262
# comparisons while the dictionary costs 317 including its build cost.


# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict
# TODO: replace the text below with your AI's claim, word for word
ai_claim = (
    "Python dictionary lookup takes O(1) time on average, while linear search takes O(n) "
    "time in the worst case, where n is the number of items. Dictionaries generally make "
    "repeated lookups faster as the collection grows, but there is no fixed speedup; "
    "actual performance depends on the data and lookup patterns and should be measured. "
    "Building a dictionary takes O(n) time on average and additional memory, so include "
    "that setup cost when comparing the total work."
)
print("AI CLAIM:", ai_claim)

# TODO: unpack find_linear() for swipes[0] into `_, front_count`
# TODO: unpack find_linear() for "M1313" into `_, absent_count`
# TODO: assign `ratio` to round(linear_running / dict_running, 1)

_, front_count = find_linear(members, swipes[0])

_, absent_count = find_linear(members, "m1313")

ratio = round(linear_running / dict_running, 1)

print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
      "| ratio:", ratio)

# TODO: replace the text below with your own verdict
verdict = "It looks like the dictionary look up was way faster as in some cases only took 1 lookup compared to linear where it took up to almost 3000 checks compared to 332 check with dictionary."
print("VERDICT:", verdict)

# Step 4, answer 1:
# The claim matched the idea that dictionary lookup is faster for
# repeated searches, but there is no one fixed speedup. The first swipe
# is 4 comparisons versus 1, a non-member is 312 versus 1, and the
# whole morning is 2924 versus 332 (about 8.8 times).


# Step 4, answer 2:
# The claim says to include the dictionary's build cost. The build cost
# was 312 steps, so the whole-morning dictionary total was 332, not 20.
