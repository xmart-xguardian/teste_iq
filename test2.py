import zipfile

with zipfile.ZipFile('C:\\Users\\Administrador\\Documents\\scans\\WebGoat.zip') as z:
    for info in z.infolist():
        print(info.filename)