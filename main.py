import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPENWEATHER_API_KEY")

def main():
    print("Hello from brambles-clothing-agent!")


if __name__ == "__main__":
    main()
