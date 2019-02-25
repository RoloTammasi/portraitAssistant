# portraitAssistant
A three pronged approach.
</br></br>
## Prong 1 - DONE
Iterate through a CSV of students and create a QR code for each student. Folder of QRs can then be uploaded to Google Drive.
Usage: 
1. Open `qr_create.py` and modify variables under `# set variable(s)`
2. Run file: `$ python qr_create.py`
</br></br>
## Prong 2 - TESTING
Iterate through a folder of images and sort pictures into separate folders per student with naming structure `LastnameFirstnameStudentID`. No need to change file name of images.
</br></br>
## Prong 3
Iterate through a folder of folders, copy last image in every folder, rename image to `[studentID].jpg`, and store in a single folder.
