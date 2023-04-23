import requests
from pyfiglet import Figlet
import folium

def get_info_by_ip(ip):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        #print(response)
        data = {
            "[Operation status]": response.get("status"),
            "[IP]": response.get("query"),
            "[Internet provider]": response.get("isp"),
            "[Country]": response.get("country"),
            "[City]": response.get("city"),
            "[Region Name]": response.get("regionName"),
            "[Organization]": response.get("org"),
            "[Postal code]": response.get("zip"),
            "[Latitude(широта)]": response.get("lat"),
            "[Longitude(довгота)]": response.get("lon")
        }

        for k, v in data.items():
            print(f"{k} : {v}")

        #area = folium.Map(location=[response.get("lat"), response.get("lon")])
        #area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print("[!]  Please check your internet connection!")

def main():
    preview_text = Figlet(font="slant")
    print(preview_text.renderText("IP INFO"))
    ip = input("Please enter your target IP: ")

    get_info_by_ip(ip = ip)


if __name__ == "__main__":
    main()
