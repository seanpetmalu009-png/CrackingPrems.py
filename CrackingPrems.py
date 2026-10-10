#!/usr/bin/env python3
"""
NIKAA FLARE — A retro hacker-style CLI tool for Android Termux.
Demo login screens + Telegram community link.
 real credentials collected. Terminal-based only.
"""

import os
import sys
import time
import platform
from datetime import datetime

# Colorama for cross-platform color support
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    # Fallback if colorama not installed
    class Fore:
        CYAN = '\033[96m'
        MAGENTA = '\033[95m'
        YELLOW = '\033[93m'
        GREEN = '\033[92m'
        RED = '\033[91m'
        WHITE = '\033[97m'
        BLACK = '\033[90m'
    class Back:
        BLACK = '\033[40m'
        CYAN = '\033[46m'
        MAGENTA = '\033[45m'
    class Style:
        RESET_ALL = '\033[0m'
        BRIGHT = '\033[1m'

NIKAA_VERSION = "1.0.0"
TELEGRAM_URL = "https://t.me/nikaascorner"

# Paid accounts (internationally created,  real credentials)
PAID_ACCOUNTS = {
    "disney_accts": {
        "username": "mike chesse",
        "password": "mickey2026!",
        "service": "Disney+"
    },
  relix_accts": {
        "username": "Sandradds@gmail.com",
        "password": "N1023970P",
        "service": "Netflix"
    }
}

def clear_screen():
    """Clear terminal screen cross-platform."""
    os.system("clear" if os.name == "posix" else "cls")

def print_banner():
    """Display large neon-style ASCII banner."""
    banner = f"""{Fore.CYAN}{Style.BRIGHT}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ███╗   ██╗██╗██╗  ██╗ █████╗  █████╗     ███████╗██╗      ║
║  ████╗  ██║██║██║ ██╔╝██╔══██╗██╔══██╗    ██╔════╝██║      ║
║  ██╔██╗ ██║██║█████╔╝ ███████║███████║    █████╗  ██║      ║
║  ██║╚██╗██║██║██╔═██╗ ██╔══██║██╔══██║    ██╔══╝  ██║      ║
║  ██║ ╚████║██║██║  ██╗██║  ██║██║  ██║    ██║     ███████╗ ║
║  ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ║
║                                                              ║
║  {Fore.MAGENTA}RETRO HACKER MENU — NEON VIBES{Fore.CYAN}                    ║
║  {Fore.YELLOW}v{NIKAA_VERSION} | Terminal-Based Demo Tool{Fore.CYAN}          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}"""
    print(banner)

def print_menu():
    """Print main menu with colorful styling."""
    menu = f"""{Fore.GREEN}{Style.BRIGHT}
┌─────────────────────────────────────────────────────┐
│  {Fore.CYAN}MAIN MENU{Fore.GREEN}                                │
├─────────────────────────────────────────────────────┤
│                                                     │
│  {Fore.YELLOW}[1]{Fore.GREEN} Disney+ Access       {Fore.WHITE}( Login){Fore.GREEN}     │
│  {Fore.YELLOW}[2]{Fore.GREEN} Netflix Access       {Fore.WHITE}(Login){Fore.GREEN}     │
│  {Fore.YELLOW}[3]{Fore.GREEN} Open Telegram       {Fore.WHITE}(Community){Fore.GREEN}      │
│  {Fore.YELLOW}[0]{Fore.GREEN} Exit                {Fore.WHITE}(Quit App){Fore.GREEN}       │
│                                                     │
└─────────────────────────────────────────────────────┘
{Style.RESET_ALL}"""
    print(menu)

def print_status():
    """Print system status bar."""
    status = f"{Fore.BLACK}{Back.CYAN} NIKAA FLARE v{NIKAA_VERSION} {Style.RESET_ALL} {Fore.CYAN}| Status: {Fore.GREEN}ONLINE{Fore.CYAN} | {datetime.now().strftime('%H:%M:%S')}{Style.RESET_ALL}"
    print(status)
    print()

def prompt_input(prompt_text):
    """Get user input with styling."""
    return input(f"{Fore.YELLOW}{Style.BRIGHT}➜ {prompt_text}{Style.RESET_ALL} ")

def display_paid_login(service_type):
    """
    Display paid login screen for Disney+ or Netflix.
    collect real credentials.
    Clearly labeled as Real.
    """
    clear_screen()
    print_banner()
    
    account_key = "disney" if service_type == "disney" else "netflix"
    account = PAID_ACCOUNTS[account_key]
    service_name = account["service"]
    
    login_screen = f"""{Fore.MAGENTA}{Style.BRIGHT}
╔═══════════════════════════════════════════════════════╗
║                  ⚠️   LOGIN SCREEN  ⚠️             ║
║                                                       ║
║  {Fore.CYAN}Service: {Fore.YELLOW}{service_name}{Fore.MAGENTA}                          ║
║  {Fore.CYAN}Mode: LOCAL PAID ACCOUNT{Fore.MAGENTA}                     ║
║                                                       ║
║  This is a local PAID. Real {service_name} credentials  ║
║   collected or transmitted.                           ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝

{Fore.GREEN}PAID Credentials (TESTING Only):{Fore.CYAN}

  Username: {Fore.YELLOW}{account['username']}{Fore.CYAN}
  Password: {Fore.YELLOW}{account['password']}{Fore.CYAN}

{Fore.WHITE}[NOTE] These are PAID credentials for testing purposes only.
        real account data is being used.{Style.RESET_ALL}

"""
    print(login_screen)
    
    # Simulate login attempt
    attempt = prompt_input("Press ENTER to simulate login or type 'back' to return to menu")
    
    if attempt.lower() == "back":
        return
    
    print(f"{Fore.CYAN}Authenticating...{Style.RESET_ALL}")
    time.sleep(1)
    print(f"{Fore.GREEN}✓ Login successful!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Welcome to {service_name} Demo{Style.RESET_ALL}")
    time.sleep(1)
    
    prompt_input("Press ENTER to return to menu")

def open_telegram():
    """Open Telegram link using system browser or Telegram app."""
    clear_screen()
    print_banner()
    
    open_screen = f"""{Fore.CYAN}{Style.BRIGHT}
╔═══════════════════════════════════════════════════════╗
║        OPENING MY TELEGRAM COMMUNITY...              ║
╚═══════════════════════════════════════════════════════╝

{Fore.MAGENTA}Community Link:{Fore.YELLOW}
  {TELEGRAM_URL}

{Fore.GREEN}Opening browser/Telegram app...{Style.RESET_ALL}
"""
    print(open_screen)
    
    try:
        if platform.system() == "Linux":
            # Termux + Android
            os.system(f"am start -a android.intent.action.VIEW -d '{TELEGRAM_URL}' 2>/dev/null || xdg-open '{TELEGRAM_URL}' 2>/dev/null")
        elif platform.system() == "Darwin":
            # macOS
            os.system(f"open '{TELEGRAM_URL}'")
        elif platform.system() == "Windows":
            # Windows
            os.startfile(TELEGRAM_URL)
        else:
            # Fallback
            os.system(f"xdg-open '{TELEGRAM_URL}' 2>/dev/null || echo 'Please visit: {TELEGRAM_URL}'")
        
        time.sleep(2)
        print(f"{Fore.GREEN}✓ Link opened!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Manual link: {TELEGRAM_URL}{Style.RESET_ALL}")
    
    time.sleep(1)
    prompt_input("Press ENTER to return to menu")

def show_about():
    """Display about/version info."""
    clear_screen()
    print_banner()
    
    about = f"""{Fore.CYAN}{Style.BRIGHT}
╔═══════════════════════════════════════════════════════╗
║                   ABOUT NIKAA FLARE                  ║
╚═══════════════════════════════════════════════════════╝

{Fore.GREEN}Version:{Fore.WHITE} {NIKAA_VERSION}
{Fore.GREEN}Type:{Fore.WHITE} Terminal CLI (Retro Hacker Style)
{Fore.GREEN}Platform:{Fore.WHITE} Android Termux + Desktop

{Fore.MAGENTA}Features:{Fore.CYAN}
  • Neon-style ASCII banner
  • Paid login screens (paid credentials)
  • Colorful retro menu interface
  • Telegram community link opener
  • Local Paid accounts for testing

{Fore.YELLOW}⚠️  SECURITY NOTES:{Fore.CYAN}
  •  real streaming credentials collected
  •  account hacking or bypassing
  •  accounts for testing only
  • Terminal-based, no web impersonation

{Fore.GREEN}Community:{Fore.WHITE}
  {TELEGRAM_URL}

{Style.RESET_ALL}"""
    print(about)
    prompt_input("Press ENTER to return to menu")

def main_loop():
    """Main application loop."""
    while True:
        clear_screen()
        print_banner()
        print_status()
        print_menu()
        
        choice = prompt_input("Select an option")
        
        if choice == "1":
            display_demo_login("disney")
        elif choice == "2":
            display_demo_login("netflix")
        elif choice == "3":
            open_telegram()
        elif choice == "0":
            clear_screen()
            exit_screen = f"""{Fore.MAGENTA}{Style.BRIGHT}
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║  {Fore.CYAN}Thanks for using NIKAA FLARE{Fore.MAGENTA}                 ║
║  {Fore.YELLOW}v{NIKAA_VERSION} | See you soon{Fore.MAGENTA}                     ║
║                                                       ║
║  {Fore.GREEN}Join us: {TELEGRAM_URL}{Fore.MAGENTA}  ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
{Style.RESET_ALL}"""
            print(exit_screen)
            sys.exit(0)
        else:
            error_msg = f"{Fore.RED}{Style.BRIGHT}✗ Invalid option. Please select 0-3.{Style.RESET_ALL}"
            print(error_msg)
            time.sleep(1)

def main():
    """Entry point."""
    try:
        main_loop()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Application interrupted.{Style.RESET_ALL}")
        sys.exit(0)

if __name__ == "__main__":
    main()
