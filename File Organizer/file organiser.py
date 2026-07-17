# os.getcwd()                                            => get current working directory
# os.chdir(<path>)                                    => change directory
# os.listdir()	                                            => list directory
# os.mkdir(<dirname>)                           => create a directory
# os.makedirs(<dirname>)                    => make directories recursively
# os.rmdir(<dirname>)	                   => remove directory
# os.removedirs(<dirname>)                => remove directory recursively
# os.rename(<from>, <to>)                   => rename file
# os.stat(<filename>)                            => print all info of a file
# os.walk(<path>)	                          => traverse directory recursively
# os.environ		                                 => get environment variables
# os.path.join(<path>, <file>)              => join path without worrying about /
# os.path.basename(<filename>)     => get basename
# os.path.dirname(<filename>)         => get dirname
# os.path.exists(<path-to-file>)         => check if the path exists or not
# os.path.splitext(<path-to-file>)      => split path and file extension
# dir(os)			                               => check what methods exists
import os

os.chdir("/Users/benedict/Downloads/downloads copy")
files = os.listdir()

os.makedirs("documents", exist_ok=True)
os.makedirs("photos", exist_ok=True)
os.makedirs("folders", exist_ok=True)
os.makedirs("videos", exist_ok=True)
os.makedirs("installers", exist_ok=True)
os.makedirs("audios", exist_ok=True)
os.makedirs("others", exist_ok=True)

index = 0


while index < len(files):
    file_name = files[index]
    path_of_file = os.path.abspath(files[index])
    splited_filename = os.path.splitext(path_of_file)

    if splited_filename[1] == ".jpg":
        new_path = "/Users/benedict/Downloads/downloads copy" + "/photos/" + file_name
        print(new_path)
        os.rename(path_of_file, new_path)

    if splited_filename[1] == ".png":
        new_path = "/Users/benedict/Downloads/downloads copy" + "/photos/" + file_name
        print(new_path)
        os.rename(path_of_file, new_path)
    if splited_filename[1] == ".jpeg":
        new_path = "/Users/benedict/Downloads/downloads copy" + "/photos/" + file_name
        print(new_path)
        os.rename(path_of_file, new_path)

    if splited_filename[1] == ".pdf":
        new_path = "/Users/benedict/Downloads/downloads copy" + "/documents/" + file_name
        print(new_path)
        os.rename(path_of_file, new_path)
    if splited_filename[1] == ".docx":
        new_path = "/Users/benedict/Downloads/downloads copy" + "/documents/" + file_name
        print(new_path)
        os.rename(path_of_file, new_path)
    if splited_filename[1] == ".zip":
        new_path = "/Users/benedict/Downloads/downloads copy" + "/documents/" + file_name
        print(new_path)
        os.rename(path_of_file, new_path)
    if splited_filename[1] == ".apk":
        new_path = "/Users/benedict/Downloads/downloads copy" + "/installers/" + file_name
        print(new_path)
        os.rename(path_of_file, new_path)
    if splited_filename[1] == ".dmg":
        new_path = "/Users/benedict/Downloads/downloads copy" + "/installers/" + file_name
        print(new_path)
        os.rename(path_of_file, new_path)
    if splited_filename[1] == ".mp3":
        new_path = "/Users/benedict/Downloads/downloads copy" + "/audios/" + file_name
        print(new_path)
        os.rename(path_of_file, new_path)
    elif os.path.isfile(path_of_file):
        new_path = "/Users/benedict/Downloads/downloads copy" + "/others/" + file_name
        print(new_path)
        os.rename(path_of_file, new_path)

    index += 1
