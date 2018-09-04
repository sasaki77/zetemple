import csv


def read_config(csvfile):
    hosts = []
    with open(csvfile, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if len(row) < 2:
                continue

            name = row[0].strip()

            if name.startswith("#"):
                continue

            prefix = row[1].strip()

            host = {'name': name, 'prefix': prefix}
            hosts.append(host)

    return hosts
