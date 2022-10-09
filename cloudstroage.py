import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from,"rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BQ2Y2SE8ix95ANy3nsL4iOYOh-AbABGDDa-A1v24gv5vRaGKSIDl5QliMyENtV94KejaJL1RjDGHLDgojx9N1xhjO3KMjtFHlpacmz10v8IuYh8ExL_Et47vxgL29p15k_9Nyt8'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer:-")
    file_to = input("enter the full path to dropbox:-")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has to be moved")


main()
