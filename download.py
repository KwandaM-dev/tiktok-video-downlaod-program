import requests

def download_tiktok_video_no_watermark():
    url = input("Enter the URL of the tiktok video: ").strip()

    api_url = f"https://www.tikwm.com/api/?url={url}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        if "data" in data and "play" in data ["data"]:
            video_url = data["data"]["play"]
            video_content = requests.get(video_url).content
            with open("tiktok.mp4", "wb") as file:
                file.write(video_content)
            print("downloaded")
        else:
            print("couldn't download")
    except Exception as e:
        print("Error" , e)

if __name__ == "__main__":
    download_tiktok_video_no_watermark()