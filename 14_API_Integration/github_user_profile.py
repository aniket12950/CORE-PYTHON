import requests

BASE_URL = "https://api.github.com/users/"

def get_github_user(username):
    try:
        url = BASE_URL + username
        response = requests.get(url, timeout=5)

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            data = response.json()

            print("\nGitHub User Details")
            print("------------------------")
            print(f" Name: {data.get('name')}")
            print(f" Username: {data.get('login')}")
            print(f" Public Repos: {data.get('public_repos')}")
            print(f" Followers: {data.get('followers')}")
            print(f" Location: {data.get('location')}")
            print(f" Profile URL: {data.get('html_url')}")

        elif response.status_code == 404:
            print(" User not found.")
        else:
            print(" Error:", response.json().get("message"))

    except requests.exceptions.Timeout:
        print(" Request timed out.")
    except requests.exceptions.ConnectionError:
        print(" Internet connection error.")
    except Exception as e:
        print(" Unexpected error:", e)


if __name__ == "__main__":
    username = input("Enter GitHub username: ").strip()
    if username:
        get_github_user(username)
    else:
        print("Please enter a valid username.")
