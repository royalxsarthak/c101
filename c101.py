import dropbox
import os
from dropbox.files import WriteMode
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

        for root,dirs, files in os.walk(file_from):

            for filename in files:

                local_Path = os.path.join(root,filename)
                
                releative_path=os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,releative_path)

                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.AxV7xs-eVjWkiBAa7p4o5My7K5-wfbIwQNNREQ2vbVmo7znzOpGDRngsQlTEfoq438MgEsh0ZKCdz-5Sj5ApyWv5Tjbf9kLjFy4rV4L5c2gLFjdCq6N7_Q17z5Tu71QAnUhpZxE'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ") 
    transferData.upload_file(file_from, file_to) 
    print("file has been moved !!!")

main()