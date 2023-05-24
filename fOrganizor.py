import os
import shutil
import sys

# print(f'Here: {os.getcwd()} ')
# shutil.move("funn.py","pythonProject")
# print(os.listdir())

def organize(path):
    correctPath = False

    audio = [".mp3", ".wav", ".aac", ".flac", ".wma", ".m4a"]
    video = [".mp4", ".avi", ".mov", ".wmv", ".mkv"]
    image = [".jpg", ".png", ".gif", ".bmp", ".svg", ".jpeg"]
    documents = [".doc", ".docx", ".docm", ".pdf", ".odt", ".xlsx", ".odp"]
    zipF =[".zip", ".7zip"]
    pwp = [".ppt", ".pptx"]
    text = [".txt"]
    icon = [".ico"]
    exe = [".exe"]
            
    is_audio = lambda file: os.path.splitext(file)[1] in audio
    is_video = lambda file: os.path.splitext(file)[1] in video
    is_image = lambda file: os.path.splitext(file)[1] in image
    is_documents = lambda file: os.path.splitext(file)[1] in documents
    is_pwp = lambda file: os.path.splitext(file)[1] in pwp
    is_txt = lambda file: os.path.splitext(file)[1] in text
    is_zip = lambda file: os.path.splitext(file)[1] in zipF
    is_exe = lambda file: os.path.splitext(file)[1] in exe
    is_icon = lambda file: os.path.splitext(file)[1] in icon

    # def is_audio(file):
    #     return os.path.splitext(file) [1] in audio # returns True if exrtention is in audio

    def moveFile(folderName):
        if os.path.exists(f"{path}\\{folderName}") == False:
            os.mkdir(folderName)
        shutil.move(file, f"{path}\\{folderName}")

    try:
        os.chdir(f"{path}")
        correctPath = True
    except:
        print("Path is empty or not existing!")
        correctPath = False

    for file in os.listdir():
        if os.path.isdir(file):
            continue
        try:
            if is_audio(file):
                moveFile("audio")
            elif is_video(file):
                moveFile("video")
            elif is_image(file):
                moveFile("image")
            elif is_documents(file):
                moveFile("documents")
            elif is_pwp(file):
                moveFile("pwp")
            elif is_txt(file):
                moveFile("text")
            elif is_zip(file):
                moveFile("zipF")
            elif is_icon(file):
                moveFile("icon")
            elif is_exe(file):
                moveFile("exe")
        except Exception as e:
            print(f"An error occurred while processing {file}: {str(e)}")
        
    return correctPath
    
        # if os.path.exists(r"C:\Users\filip\Downloads\test\audio") == False:
        #     os.mkdir("audio")
        # shutil.move(file,r"C:\Users\filip\Downloads\test\audio")

if __name__ == "__main__":
    # print(sys.argv)
    organize(sys.argv[1])