import csv


class SenderConfigReaderCSV(object):
    def __init__(self):
        pass

    def read_config(self, csvfile):
        hosts = []
        with open(csvfile, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                host = {}
                host['name'] = row[0].strip()
                host['prefix'] = row[1].strip()
                hosts.append(host)

        return hosts
