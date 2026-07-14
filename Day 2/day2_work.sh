#creating directory
mkdir case_study
echo "Directory create"
cd case_study
echo "Path changed"
pwd

#creating file
touch file1.txt file2.txt
echo "Files created"
#structure
echo "File structure of case_Study" 
ls

#writing content into file1.txt
echo "This is text file one content">file1.txt
echo "Text is written in file1.txt"
echo
cat file1.txt
echo


#copy file content from file1 to file2
cp file1.txt file2.txt
echo "Content from file1.txt is moved to file2.txt"
echo
cat file2.txt
echo

#rename file
mv file1.txt rename_file1.txt
echo "File1.txt is renamed"
echo


#search for specific file
find . -name "file2.txt"
echo "file found"
#set permissions on a script
chmod +x file2.txt
echo
echo "file permission on file2.txt"
ls -l
echo


#compress the project into .tar archive
mkdir tarfolder
cd tarfolder
touch demo1.txt demo2.txt
cd ..

tar -cvf tarfile.tar tarfolder/


#extract it to a new location
mkdir recovery
tar -xvf tarfile.tar -C recovery

#verify final structure
echo "final file structure"
ls 
