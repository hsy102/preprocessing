<readme>



# 1. unpair_move_and_log.py

	After checking the image and XML pairs, unpaired files are moved to the newly created 'unpair' folder along with the creation of log files.

command : python unpair_move_and_log.py --checkunpair "path"





# 2. nodedelete.py

	1) x == y : object delete
	2) x, y < 0 : x == 0, y == 0
	3) x, y > width, height : x/y_min, x/y_max == width, height

command : python nodedelete.py --nodedelete "path"

