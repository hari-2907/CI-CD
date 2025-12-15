import requests

def check_app(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ App is UP at {url}")
        else:
            print(f"⚠️ App returned status {response.status_code}")
    except Exception as e:
        print(f"❌ App is DOWN. Error: {e}")

if __name__ == "__main__":
    # Replace with your EC2 public DNS or app URL
    check_app("http://your-ec2-public-dns:8080")
