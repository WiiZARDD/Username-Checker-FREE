import os
import csv
from datetime import datetime
import requests
from colorama import Fore, Style, init

# Initialize colorama for cross-platform ANSI color support
init()

# List of popular social media platforms and services
PLATFORMS = [
    "facebook",
    "twitter",
    "instagram",
    "snapchat",
    "tiktok",
    "youtube",
    "discord",
    "guilded",
    "pinterest",
    "tumblr",
    "reddit",
    "whatsapp",
    "kik",
    "wechat",
    "viber",
    "quora",
    "tinder",
    "grindr",
    "hinge",
    "bumble",
    "okcupid",
    "zoosk",
    "replit",
    "github",
]

LOG_FILE = "username_checker_log.csv"


def check_username(username):
    results = {}

    for platform in PLATFORMS:
        platform_result = {"platform": platform, "available": False}

        # Implement the code to check username availability on each platform
        available = check_availability(platform, username)
        platform_result["available"] = available

        results[platform] = platform_result

    return results


def check_availability(platform, username):
    # Implement username availability using web scraping
    # This is a simplified example and may require updates if website structures change
    url = f"https://www.{platform}.com/{username}/"
    response = requests.get(url)
    return response.status_code == 404


def save_to_log(username, results):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append the results to the log file
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        for platform, result in results.items():
            status = "Available" if result["available"] else "Taken"
            writer.writerow([timestamp, username, platform, status])


def display_results(results):
    print("\nResults:")
    for platform, result in results.items():
        status = "Available" if result["available"] else "Taken"
        print(f"{platform}: {Fore.GREEN if result['available'] else Fore.RED}{status}{Style.RESET_ALL}")


def print_header():
    print(f"{Fore.CYAN}╔════════════════════════════════════════════════════╗")
    print(f"{Fore.CYAN}║{Style.RESET_ALL}           Social Media Username Checker            {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Style.RESET_ALL}            ~~~~~~ Pro Edition ~~~~~~               {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Style.RESET_ALL}               Developed by WiIZARDD                {Fore.CYAN}║")
    print(f"{Fore.CYAN}╚════════════════════════════════════════════════════╝")
    print(f"{Fore.CYAN}           [Note: Spam leads to Rate Limits]          {Style.RESET_ALL}\n")


def main():
    os.system("clear" if os.name == "posix" else "cls")
    print_header()

    while True:
        print(f"{Fore.MAGENTA}Menu:{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}1. Check Username Availability{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}2. View Log{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}3. Exit{Style.RESET_ALL}")
        choice = input(f"{Fore.YELLOW}Enter your choice (1/2/3): {Style.RESET_ALL}")

        if choice == "1":
            username = input(f"{Fore.YELLOW}Enter the username you want to check: {Style.RESET_ALL}")
            results = check_username(username)
            display_results(results)
            save_to_log(username, results)
        elif choice == "2":
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, newline="") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(
                            f"Timestamp: {row[0]}, Username: {row[1]}, Platform: {row[2]}, Status: {row[3]}"
                        )
            else:
                print(f"{Fore.YELLOW}Log file is empty.{Style.RESET_ALL}")
        elif choice == "3":
            print(f"{Fore.CYAN}Thank you for using the Social Media Username Checker!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please choose a valid option.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
