import platform
import os

# Códigos de cores ANSI
RESET = "\033[0m"
GREEN = "\033[32m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"


def get_processor_info():
    system = platform.system()
    architecture = platform.architecture()[0]
    processor = ''
    if system == "Windows":
        processor = platform.processor()
    elif system in ["Linux", "Darwin"]:  # Darwin é o nome do sistema para macOS
        try:
            if system == "Linux":
                with open("/proc/cpuinfo") as f:
                    cpuinfo = f.read()
                    if "model name" in cpuinfo:
                        processor = cpuinfo.split("model name")[1].split(":")[1].split("\n")[0].strip()
                    else:
                        processor = "Unknown"
            elif system == "Darwin":
                processor = os.popen("sysctl -n machdep.cpu.brand_string").read().strip()
        except FileNotFoundError:
            processor = "Unknown"

    return (f"{BLUE}System:{RESET} {GREEN}{system}{RESET}\n"
            f"{BLUE}Architecture:{RESET} {CYAN}{architecture}{RESET}\n"
            f"{BLUE}Processor:{RESET} {MAGENTA}{processor}{RESET}")


print(get_processor_info())
