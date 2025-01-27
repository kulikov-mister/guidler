# utils/imgur_downloader.py
from imgurpython import ImgurClient

Client_ID= "client id"
Client_secret= "secret"

client = ImgurClient(Client_ID, Client_secret)

def upload_image(image_url):
    """
    Загружает изображение на Imgur и возвращает прямую ссылку на него.
    """
    response = client.upload_from_url(image_url, anon=True)
    return response['link']

# source_image_url = "https://dayhub.ru/upload/000/u1/1/7/zhorzh-dare-photo-normal.png"
# image_url = upload_image(source_image_url)
# print(image_url)
