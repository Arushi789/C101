import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'fW-n9n5vunkAAAAAAAAAATTcp3Ohrr1i2ST6bo0DelK4ifkSm49ae75UsNH_Hb_3'
    transferData = TransferData(access_token)

    file_from = 'D:/Visual Studio Code/C101/text.txt'
    file_to = 'Dropbox/text.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved...")
if __name__ == '__main__':
    main()