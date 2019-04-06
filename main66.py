import os


def solider(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")
        for file in files:
            if file not in filelist:
                os.rename(file, file.capitalize())

            if os.path.splitext(file)[1] == format:
                os.rename(file, f"{i}{format}")
                i+= 1


# solider(r"C:\Users\krupa\Desktop\om", r"C:\Users\krupa\PycharmProjects\hello\exe.txt", ".jpg")
