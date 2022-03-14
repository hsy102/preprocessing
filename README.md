<readme>



# 1. unpair_move_and_log.py

	After checking the image and XML pairs, unpaired files are moved to the newly created 'unpair' folder along with the creation of log files.

command : python unpair_move_and_log.py --checkunpair "path"



# 2. nodedelete.py

	1) x == y : object delete
	2) x, y < 0 : x == 0, y == 0
	3) x, y > width, height : x/y_min, x/y_max == width, height

command : python nodedelete.py --nodedelete "path"



# 3. xml_object_name_classification.ipynb

1) Classified by file tool and copied.
2) Delete classes other than that class.
3) Check the quantity.



# 4. delete_specific_extension_files.ipynb

Delete specific extension files in multiple directories.



# 5. output_filenames.ipynb

Output file names in the directory.

1) Extensions included.
2) Remove extensions.
3) Delete the generated filename.txt file.



