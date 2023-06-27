<readme>



# 1. unpair_move_and_log.py

After checking the image and XML pairs, unpaired files are moved to the newly created 'unpair' folder along with the creation of log files.

command : python unpair_move_and_log.py --checkunpair "path"



# 2. nodedelete.py

	1) x == y : object delete
	2) x, y < 0 : x == 0, y == 0
	3) x, y > width, height : x/y_min, x/y_max == width, height

command : python nodedelete.py --nodedelete "path"



# 3. xml_object_classification.py

1) Classified by file Annotation Class and copied.
2) Delete classes other than that class.



# 4. delete_specific_extension_files.ipynb

Delete specific extension files in multiple directories.



# 5. output_filenames.ipynb

Output file names in the directory.

1) Extensions included.
2) Remove extensions.
3) Delete the generated filename.txt file.



# 6. extract_video_properties_and_save_as_excel.ipynb

Property type of video: filename, width, height, fps, hms, size (Starting with index 1)



# 7. change_filename.ipynb

Read column before & after change in excel file and change file name.



# 8. excel_or_csv_matrix_conversion.ipynb

Switches the positions of rows and columns in excel or csv file.



# 9. Number_of_videos_completed.ipynb

1) Number of videos and total surgeries by surgery.
2) Number of surgeries completed and total number of surgeries completed.
3) Counting the number of tools by surgery.



# 10. merging_csv_col.ipynb

Import only necessary columns from two csv files and create one file.



# 11. classify_files_by_filename.ipynb

Classify files by creating a folder with a specific string of file names.



# 12. merge_into_one_csv.ipynb

Merge all csv files and merge specific columns.



# 13. add_col_to_csv.ipynb

Add column with formula to csv file.



# 14. change_csv_15_frame.ipynb

Change the frame number of the video in units of 15 frames.



# 15. json_object_classification.py

1) Classified by file Annotation Class and copied.
2) Delete classes other than that class.



# 16. image_combine_v3.py

A script that attaches the original image and the image with annotation polygons added as lines on both sides.(Transparency adjustable)



# 17. image_combine_v4.py

A script that attaches the original image and the image with annotation rectangles added as lines on both sides.(Transparency adjustable)



# 18. gt_inference_confusion_matrix.py

A script that compares files with the same file name in the gt folder and the file name in the inference folder to obtain classification model performance evaluation indicators.

command : python gt_inference_confusion_matrix.py --gt_folder_path "GT folder path" --pred_folder_path "Inference folder path" --output_folder_path "Folder path to save results"



# 19. json_to_xml.py

Code to convert json file divided into meta folder and labels folder to xml file.

command : python json_to_xml.py --meta_folder_path "meta folder path(json)" --labels_folder_path "labels folder path(json)" --output_folder_path "folder path to save the converted xml file"
















