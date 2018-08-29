""" *****************************************************************************
          Archana Bahuguna 08/28/2018 8:30pm    rec_twrshanoi.py
           
    This python module implements the puzzle Towers of Hanoi using recursion

 *****************************************************************************
"""

print "------------------------------------------------------\n\nTowers of Hanoi\n=============\n"

num_disks = int(raw_input("Enter no. of disks > 2:"))
while (num_disks < 3):
    num_disks = int(raw_input("Error. Please enter no. of disks > 2:"))

"""Recursively moves the disks from one tower to another.

  Rules of Tower of hanoi puzzle:
  1. A larger disk can never be put on top of a smaller disk
  2. No disk can be moved to it's previous place

  takes argument: (no_disks), returns None
"""

towers = [0, 1, 2]            # List of Towers of Hanoi

disks = []                    # List of disks
for i in range(num_disks):
	disks.append(i)

# TBD -----
def pick_next_fromto_towers():

	return totower, fromtower 

def twrshanoi_move_disks(num_disks):
    
    disks_on_origtwr = num_disks
    disks_on_destntwr = 0
    curr_disk = 0

    if (disks_on_destntwr == num_disks):
    	return 1
    move(curr_disk)

    return 0

def move_disk(thisdisk, thistower):

    if disk_size(this) < disk_size(disk_on_other_tower):
    	move_this_to_other_tower

	return None


if twrshanoi_move_disks(num_disks):
	print "Successfully executed Towers of Hanoi algorithm in n moves"
else:
	print "Failed somewhere!"
# TBD -----

print "\n------------------------------------------------------"


