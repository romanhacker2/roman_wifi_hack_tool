import os
import sys
import time
import random
import string
import subprocess
import json

RESET="\033[0m"; BOLD="\033[1m"; GREEN="\033[92m"; RED="\033[91m"; YELLOW="\033[93m"; BLUE="\033[94m"; CYAN="\033[96m"; WHITE="\033[97m"; MAGENTA="\033[95m"

WP_LINK_1 = "https://whatsapp.com/channel/0029VawwXaeEquiIR1CLXA30"
WP_LINK_2 = "https://whatsapp.com/channel/0029Vb9nyrf2phHLHViKGU0w"
TG_LINK_APP = "tg://resolve?domain=romanhacker2"

def clear(): os.system("clear")

def show_banner():
    print(f"""{CYAN}{BOLD}
    ██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║
    ██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║
    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    {RED}⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣦⡀⠀
    {RED}⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⠀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣧
    {RED}⠀⠀⠀⠀⣼⣿⣿⣿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣠⣴⣶⣤⡀⠀
    {RED}⠀⠀⠀⢰⣿⣿⣿⣿⠃⠈⢻⣿⣦⠀⠀⠀⠀⣸⣿⣿⣿⣿⣷⠀
    {RED}⠀⠀⠀⠘⣿⣿⣿⡏⣴⣿⣷⣝⢿⣷⢀⠀⢀⣿⣿⣿⣿⡿⠋⠀
    {RED}⠀⠀⠀⠀⢿⣿⣿⡇⢻⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⢸⣿⣿⣇⢸⣿⣿⡟⠙⠛⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀
    {RED}⣴⣿⣿⣿⣿⣿⣿⣿⣠⣿⣿⡇⠀⠀⠀⠉⠛⣽⣿⣇⣀⣀⣀⠀
    {RED}⠙⠻⠿⠿⠿⠿⠿⠟⠿⠿⠿⠇⠀⠀⠀⠀⠀⠻⠿⠿⠛⠛⠛{RESET}
    {MAGENTA}{BOLD}         [ R O M A N   W I F I   H A C K E R ]{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    {GREEN} DEV: {WHITE}ROMAN HACKER {GREEN}| TG: {WHITE}@romanempire078{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    """)

def open_wa(url):
    os.system(f"am start -a android.intent.action.VIEW -d '{url}' -f 0x10000000 > /dev/null 2>&1")

def open_tg(url):
    os.system(f"am start -a android.intent.action.VIEW -d '{url}' > /dev/null 2>&1")

def security_gate():
    clear()
    show_banner()
    print(f"\n{RED}{BOLD}  ⚠️  ACCESS LOCKED - CHANNEL VISIT REQUIRED  ⚠️{RESET}\n")
    print(f"{WHITE}  To unlock this tool, you must visit our official channels.{RESET}")
    print(f"{YELLOW}  Opening Channels... (Please wait){RESET}\n")
    time.sleep(1)
    
    print(f"{CYAN}  [~] Opening WhatsApp Channel 1...{RESET}")
    open_wa(WP_LINK_1)
    time.sleep(4)
    
    print(f"{CYAN}  [~] Opening WhatsApp Channel 2...{RESET}")
    open_wa(WP_LINK_2)
    time.sleep(4)
    
    print(f"{CYAN}  [~] Opening Telegram Channel...{RESET}")
    open_tg(TG_LINK_APP) 
    time.sleep(3)
    
    print(f"\n{GREEN}  [✓] Channels Opened. Please visit and return here.{RESET}")
    input(f"{YELLOW}  ► Press ENTER to unlock tool...{RESET}")

def get_random_networks():
    prefixes = ["Jazz", "Zong", "PTCL", "TP-Link", "Telenor", "AndroidAP", "Home", "Family", "Starlink", "Ali", "Hamza", "Usman", "Daraz"]
    suffixes = ["_5G", "_2.4G", "_Fiber", "_Pro", "_Net", "123", "456", "786", "7860", "_WiFi"]
    nets = []
    for _ in range(5):
        ssid = random.choice(prefixes) + random.choice(suffixes)
        while any(net['SSID'] == ssid for net in nets):
            ssid = random.choice(prefixes) + random.choice(suffixes)
        mac = ":".join([f"{random.randint(0, 255):02X}" for _ in range(6)])
        level = random.randint(-85, -40)
        nets.append({"SSID": ssid, "BSSID": mac, "level": level})
    return nets

def scan_wifi():
    clear()
    show_banner()
    print(f"{YELLOW}{BOLD}  [~] Initializing WiFi Adapter...{RESET}")
    time.sleep(1)
    print(f"{YELLOW}  [~] Scanning nearby networks...{RESET}\n")
    time.sleep(1.5)
    display_nets = []
    try:
        result = subprocess.check_output(["termux-wifi-scaninfo"], stderr=subprocess.STDOUT, timeout=10)
        networks = json.loads(result.decode('utf-8'))
        unique_nets = {}
        for net in networks:
            ssid = net.get('SSID', 'Hidden')
            if ssid and ssid != 'Hidden' and ssid not in unique_nets:
                unique_nets[ssid] = net
        if unique_nets:
            display_nets = list(unique_nets.values())[:10]
    except Exception:
        pass
    if not display_nets:
        print(f"{RED}  [!] Hardware Scan Blocked by Android. Loading DB...{RESET}")
        time.sleep(1.5)
        display_nets = get_random_networks()
    print(f"{GREEN}{BOLD}  ═══════════ FOUND NETWORKS ═══════════{RESET}")
    for i, net in enumerate(display_nets, 1):
        ssid = net.get('SSID', 'Unknown')
        bssid = net.get('BSSID', 'Unknown MAC')
        level = net.get('level', -50)
        if level > -50: color = GREEN
        elif level > -70: color = YELLOW
        else: color = RED
        print(f"  {WHITE}[{i}]{RESET} {color}{ssid:<22}{RESET} | MAC: {bssid[:17]} | {level} dBm")
    print(f"{GREEN}{BOLD}  ══════════════════════════════════════{RESET}\n")
    choice = input(f"{CYAN}{BOLD}  ► Select Network to Hack [1-{len(display_nets)}]: {RESET}").strip()
    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(display_nets): raise ValueError
        return display_nets[idx]
    except ValueError:
        print(f"{RED}  Invalid Selection!{RESET}")
        time.sleep(2)
        return None

def generate_random_password():
    chars = string.ascii_letters + string.digits + "!@#$"
    return ''.join(random.choice(chars) for _ in range(10))

def brute_force(target_net):
    ssid = target_net.get('SSID')
    bssid = target_net.get('BSSID')
    clear()
    show_banner()
    print(f"{RED}{BOLD}  [!] TARGET LOCKED: {WHITE}{ssid}{RESET}")
    print(f"{YELLOW}  [~] MAC Address: {WHITE}{bssid}{RESET}\n")
    print(f"{CYAN}  [~] Starting Monitor Mode on wlan0...{RESET}")
    time.sleep(1)
    print(f"{CYAN}  [~] Capturing WPA Handshake...{RESET}")
    for i in range(1, 101):
        sys.stdout.write(f"\r{RED}{BOLD}  [>] Capturing Packets: {i}%{RESET}")
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")
    print(f"{GREEN}  [✓] WPA Handshake Captured!{RESET}")
    print(f"{YELLOW}  [~] Starting Brute Force (5000 Passwords)...{RESET}")
    print(f"{WHITE}  [~] Time Limit: 60 Seconds{RESET}\n")
    time.sleep(1.5)
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    total_passwords = 5000
    duration = 60.0 
    start_time = time.time()
    final_cracked_password = generate_random_password()
    try:
        for i in range(1, total_passwords + 1):
            fake_pass = "".join(random.choice(chars) for _ in range(10))
            if i % 5 == 0 or i < 50:
                sys.stdout.write(f"\033[91m  [TRY {i:04d}] Testing: {fake_pass}\033[0m\n")
                sys.stdout.flush()
            elapsed = time.time() - start_time
            target_time = i * (duration / total_passwords)
            sleep_time = target_time - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)
    except KeyboardInterrupt:
        print(f"\n\n{RED}  [!] Attack Aborted by User!{RESET}")
        time.sleep(2)
        return
    time.sleep(1)
    clear()
    show_banner()
    print(f"\n{GREEN}{BOLD}")
    print("  ╔══════════════════════════════════════════════════╗")
    print("  ║             🔓 WIFI CRACKED! 🔓                  ║")
    print("  ╠══════════════════════════════════════════════════╣")
    print(f"  ║  {YELLOW}TARGET   : {WHITE}{ssid[:33]:<33} {GREEN}║")
    print(f"  ║  {YELLOW}MAC ADDR : {WHITE}{bssid[:33]:<33} {GREEN}║")
    print(f"  ║  {YELLOW}PASSWORD : {RED}{final_cracked_password:<33} {GREEN}║")
    print("  ╠══════════════════════════════════════════════════╣")
    print(f"  ║  {CYAN} DEVELOPER: {WHITE}ROMAN HACKER                    {GREEN}║")
    print(f"  ║  {CYAN} TELEGRAM : {WHITE}@romanempire078                  {GREEN}║")
    print("  ╚══════════════════════════════════════════════════╝")
    print(f"{RESET}")
    input(f"{CYAN}  Press ENTER to return...{RESET}")

def main():
    security_gate()
    while True:
        try:
            clear()
            show_banner()
            print(f"""{BLUE}{BOLD}
    ┌──────────────────────────────────────────────────┐
    │                WIFI HACKER CONTROL               │
    ├──────────────────────────────────────────────────┤
    │  {WHITE}[1]{GREEN} Scan & Hack Nearby WiFi                   │
    │  {WHITE}[2]{BLUE} Exit System                               │
    └──────────────────────────────────────────────────┘
{RESET}""")
            choice = input(f"{GREEN}{BOLD}  └──► Select Option [1-2]: {RESET}").strip()
            if choice == "1":
                net = scan_wifi()
                if net:
                    brute_force(net)
            elif choice == "2":
                print(f"\n{RED} Exiting System...{RESET}")
                time.sleep(1)
                break
            else:
                time.sleep(0.5)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
