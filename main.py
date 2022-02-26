import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {"Authorization" : f'OAuth {self.token}'}

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        link_dict = self._get_upload_link(disk_file_path=disk_file_path)
        href = link_dict.get("href", "")

        response = requests.put(href, data=open(disk_file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    uploader = YaUploader('_____') # необходимо ввести токен
    result = uploader.upload("Test.txt") # необходимо ввести имя файла
