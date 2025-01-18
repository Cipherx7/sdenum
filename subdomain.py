import subprocess
import argparse
import requests
import time
import socket
import os
import json
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# Configuration file for wordlists
CONFIG_FILE = "wordlists_config.json"

# Default wordlists
DEFAULT_WORDLISTS = {
    "amass": "amass_default_wordlist.txt",
    "sublist3r": "sublist3r_default_wordlist.txt",
    "ffuf": "ffuf_default_wordlist.txt"
}

def display_banner(wordlists=None):
    print("""
                                                       Version: 1.0
      _______. _______   _______ .__   __.  __    __  .___  ___.
     /       ||       \\ |   ____||  \\ |  | |  |  |  | |   \\/   |
    |   (----`|  .--.  ||  |__   |   \\|  | |  |  |  | |  \\  /  |
     \\   \\    |  |  |  ||   __|  |  . `  | |  |  |  | |  |\\/|  |
 .----)   |   |  '--'  ||  |____ |  |\\   | |  `--'  | |  |  |  |
 |_______/    |_______/ |_______||__| \\__|  \\______/  |__|  |__|


               # Coded by c1ph3rX7 aka Abhishek Pawar

""")
    print(
        "Usage: python3 subdomain_enum.py <domain> [-a] [-u] [-f] [-w] [-q]\n"
        "Options:\n"
        "  -a    Use Amass\n"
        "  -u    Use Sublist3r\n"
        "  -f    Use FFUF\n"
        "  -w    Customize wordlists\n"
        "  -q    Quiet mode (suppress banner)\n"
        "\n"
        "Note: If no flags are provided, all tools will be used by default.\n"
    )
    if wordlists:
        print("Current Wordlists:")
        print(f"  Amass: {wordlists['amass']}")
        print(f"  Sublist3r: {wordlists['sublist3r']}")
        print(f"  FFUF: {wordlists['ffuf']}")
        print()

def load_wordlists():
    """Load wordlists from the configuration file or use defaults."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return DEFAULT_WORDLISTS.copy()

def save_wordlists(wordlists):
    """Save the custom wordlists to the configuration file."""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(wordlists, f, indent=4)
    print(f"{Fore.YELLOW}Wordlists saved to {CONFIG_FILE}.")

def get_wordlist(tool_name):
    """Prompt user to enter a custom wordlist path."""
    wordlist = input(f"Enter the wordlist path for {tool_name} (or press Enter to use default): ")
    return wordlist if wordlist else DEFAULT_WORDLISTS[tool_name]

def customize_wordlists(wordlists):
    """
    Allows the user to customize wordlists for Amass, Sublist3r, and FFUF.
    Updates and saves the configuration file.
    """
    print("Customize your wordlists for each tool:")
    print("1) Amass")
    print("2) Sublist3r")
    print("3) FFUF")
    print("4) Done")

    while True:
        choice = input("Select an option (1-4): ").strip()
        if choice == '1':
            wordlists['amass'] = get_wordlist("Amass")
        elif choice == '2':
            wordlists['sublist3r'] = get_wordlist("Sublist3r")
        elif choice == '3':
            wordlists['ffuf'] = get_wordlist("FFUF")
        elif choice == '4':
            save_wordlists(wordlists)
            print("Customization completed.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
    return wordlists

def ping_domain(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        return response.status_code
    except requests.RequestException:
        return None

def run_amass(domain, wordlist):
    subprocess.run(['amass', 'enum', '-d', domain, '-o', 'amass_output.txt', '-w', wordlist])

def run_sublist3r(domain, wordlist):
    subprocess.run(['python3', 'sublist3r.py', '-d', domain, '-o', 'sublist3r_output.txt', '-w', wordlist])

def run_ffuf(domain, wordlist):
    subprocess.run(['ffuf', '-w', wordlist, '-u', f'https://FUZZ.{domain}', '-o', 'ffuf_output.txt'])

def merge_results():
    with open('final_output.txt', 'w') as outfile:
        for filename in ['amass_output.txt', 'sublist3r_output.txt', 'ffuf_output.txt']:
            if os.path.exists(filename):
                with open(filename) as infile:
                    outfile.write(infile.read())

def main():
    parser = argparse.ArgumentParser(description='Subdomain Enumeration Tool')
    parser.add_argument('domain', type=str, nargs='?', help='The target domain to enumerate subdomains for (e.g., example.com)')
    parser.add_argument('-a', action='store_true', help='Use Amass for enumeration')
    parser.add_argument('-u', action='store_true', help='Use Sublist3r for enumeration')
    parser.add_argument('-f', action='store_true', help='Use FFUF for enumeration')
    parser.add_argument('-w', action='store_true', help='Customize wordlists')
    parser.add_argument('-q', action='store_true', help='Quiet mode (suppress banner)')
    args = parser.parse_args()

    # Load wordlists (default or previously saved)
    wordlists = load_wordlists()

    # If no arguments, show banner and exit
    if len(vars(args)) == 1 or not args.domain:
        display_banner(wordlists)
        if not args.domain:
            print(f"{Fore.RED}Error: Domain argument is required.\n")
        return

    # Customize wordlists if the -w flag is used
    if args.w:
        wordlists = customize_wordlists(wordlists)

    if not args.q:  # Display the banner if not in quiet mode
        display_banner(wordlists)

    target_domain = args.domain
    print(f"Starting checks for domain: {target_domain}")

    # Run selected tools or all by default
    if args.a:
        run_amass(target_domain, wordlists['amass'])
    if args.u:
        run_sublist3r(target_domain, wordlists['sublist3r'])
    if args.f:
        run_ffuf(target_domain, wordlists['ffuf'])
    if not (args.a or args.u or args.f):
        run_amass(target_domain, wordlists['amass'])
        run_sublist3r(target_domain, wordlists['sublist3r'])
        run_ffuf(target_domain, wordlists['ffuf'])

    merge_results()
    print(f"Subdomain enumeration completed. Results saved in final_output.txt.")

if __name__ == "__main__":
    main()
