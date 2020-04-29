import requests, json

class ShodanIO():
    def __init__(self, args, target, handler):
        self.description = "Example module"
        self.author = '@m8r0wn'
        self.method = ['scrape']

        self.handler = handler
        self.target = target

    def execute(self):
        apikey = "YOUR_API_KEY_HERE"
        domain = self.target

        r = requests.get('https://api.shodan.io/dns/domain/' + domain + '?key=' + apikey)
        data = json.loads(r.text)
        subdomains = set()
        for item in data["data"]:
            entry = item["subdomain"]
            record_type = item["type"]
            value = item["value"]
            if record_type == 'CNAME' and domain in value:
                delim = value.split('.')
                match = delim[-2] + '.' + delim[-1]
                if match == domain:
                    subdomains.add(value)
        for s in subdomains:
            sub = s
            self.handler.sub_handler({'Name': sub, 'Source': 'Shodan-IO'})








