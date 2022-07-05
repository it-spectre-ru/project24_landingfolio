import requests



headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
	"Accept-Ranges": "none"
}


def get_data_file(headers):
	url = "https://landingfolio.com/"

	r = requests.get(url=url, headers=headers)

	with open('index.html', 'w') as file:
		file.write(r.text)

def download_imgs(file_path):
	pass

def main():
	get_data_file(headers=headers)

if __name__ == '__main__':
	main()