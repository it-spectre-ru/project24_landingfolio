import json
import requests



headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
	"Accept-Ranges": "none"
}


def get_data_file(headers):
	# url = "https://landingfolio.com/"

	# r = requests.get(url=url, headers=headers)

	# with open('index.html', 'w') as file:
	# 	file.write(r.text)

	pages = 0
	result_list = []

	for i in range(1, 5):
		url = f'https://landingfolio.com/api/inspiration?page={i}'

		response = requests.get(url=url, headers=headers)
		data = response.json()

		for item in data:
				result_list.append(
					{
						"title": item.get("title"),
						"slug": item.get("slug"),
						"url": item.get("url")
					}
				)
				print(item['title'])
				with open("result_list.json", "a") as file:
					json.dump(result_list, file, indent=4, ensure_ascii=True)

				return f"[INFO] Finish"
				
		print(f"[+] Processed {i}")
		pages += 1



def download_imgs(file_path):
	pass


def main():
	print(get_data_file(headers=headers))

if __name__ == '__main__':
	main()