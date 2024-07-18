from colorama import Fore, Back, Style

print(f"{Fore.CYAN}Hello {Fore.RED}From {Fore.GREEN}colorama {Style.RESET_ALL}")
#print(Style.RESET_ALL)

print(Fore.RED + "some red text")
print(Back.GREEN + "and with a green background")
print(Style.BRIGHT + "and in bright text")
print(Style.RESET_ALL)
print("back to normal now")