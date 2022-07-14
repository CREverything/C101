import dropbox
from dropbox.files import WriteMode
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        print("Executed")
        try:
            dbx = dropbox.Dropbox(self.access_token)
            for root, dirs, files in os.walk(file_from):
                print(os.walk(file_from))
                for dir in dirs:
                    for root,dirs,files in os.walk(dir):
                        for file_name in files:
                            local_path = os.path.join(root, file_name)
                            relative_path = os.path.relpath(local_path, file_from)
                            dropbox_path = os.path.join(file_to, relative_path)
                            with open(local_path, "rb") as f:
                                dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
                                print("Your folder has been uploaded.")
                for file_name in files:
                    local_path = os.path.join(root, file_name)
                    relative_path = os.path.relpath(local_path, file_from)
                    dropbox_path = os.path.join(file_to, relative_path)
                    with open(local_path, "rb") as f:
                        dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
                        print("Your folder has been uploaded.")
        except:
            print("Error")
            print(sys.exc_info()[0]
)
        

def main():
    access_token = "sl.BK9xtuOE6X2A2IJrlCBchTSxw8YSSo07LYG-sCv6wqgQ4bCATkTp5ymYvi-ygA-0j8glNLuo92NbCUrpicHtnEkm_8l63_e0RjAkwyUXaJkUfTw358t7Z28bzBZk_A75tbw_L5mmNN2-"
    transferData = TransferData(access_token)
    file_from = str(input("Which folder would you like to upload?\n"))
    file_to = input("Which path would you like to upload to?\n")
    transferData.upload_file(file_from, file_to)

main()