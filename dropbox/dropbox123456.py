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
    access_token = 'OOnkcK7OsU4AAAAAAAAAAbEQnFSiDQCgcChCyhMJ2jcm5UH59mdyUaufW4T22ps2'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '\test\test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()