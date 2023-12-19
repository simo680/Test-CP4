import requests
import pprint


def get_random_dog_image():
    base_url = "https://dog.ceo/api"
    response = requests.get(f"{base_url}/breeds/image/random")
    data = response.json()
    pprint.pprint(data)


def get_number_of_breeds():
    base_url = "https://dog.ceo/api"
    response = requests.get(f"{base_url}/breeds/list")
    data = response.json()
    breeds_count = len(data.get("message", []))
    pprint.pprint(breeds_count)


def get_random_dog_image_by_breed(breed):
    base_url = "https://dog.ceo/api"
    response = requests.get(f"{base_url}/breed/{breed}/images/random")
    data = response.json()
    pprint.pprint(data)


def get_list_of_sub_breeds(breed):
    base_url = "https://dog.ceo/api"
    response = requests.get(f"{base_url}/breed/{breed}/list")
    data = response.json()
    pprint.pprint(data)


def get_random_dog_image_by_sub_breed(breed, sub_breed):
    base_url = "https://dog.ceo/api"
    response = requests.get(f"{base_url}/breed/{breed}/{sub_breed}/images/random")
    data = response.json()
    pprint.pprint(data)


if __name__ == '__main__':
    print("Рандомное изображение собаки:")
    get_random_dog_image()
    print("\nКоличество пород:")
    get_number_of_breeds()
    print("\nРандомное изображение собаки по породе:")
    get_random_dog_image_by_breed("pug")
    print("\nСписок подпород у породы:")
    get_list_of_sub_breeds("terrier")
    print("\nРандомное изображение собаки по подпороде:")
    get_random_dog_image_by_sub_breed("terrier", "fox")