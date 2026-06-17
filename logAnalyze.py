import re

zvit = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0,
    "Failed login": 0
}

ip_zvit = {}
target = 22


with open('server_logs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        cleaned_line = line.strip()

        if cleaned_line[target] == "I":
            zvit['INFO'] += 1
        elif cleaned_line[target] == "W":
            zvit['WARNING'] += 1
            if cleaned_line[32] == "F":
                zvit["Failed login"] += 1
                match = re.search(r"IP ([\d.]+)", line)
                if match:
                    ip_address = match.group(1)
                    if ip_address in ip_zvit:
                        ip_zvit[ip_address] += 1
                    else:
                        ip_zvit[ip_address] = 1

        elif cleaned_line[target] == "E":
            zvit['ERROR'] += 1


with open('zvit_konsoli.txt', 'w', encoding='utf-8') as f_out:
    print(zvit, file=f_out)
    print("\nСтатистика по IP-адресах:", file=f_out)
    for ip, count in ip_zvit.items():
        print(f"{ip} ({count})", file=f_out)

print(zvit)
print("\nСтатистика по IP-адресах:")
for ip, count in ip_zvit.items():
    print(f"{ip} ({count})")

print("\n[Успішно] Усі дані також скопійовано у файл 'zvit_konsoli.txt'!")
