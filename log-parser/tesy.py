def get_num_characters(text):
    dict1 = {}
    for i in text.split():
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

text = "the server crashed because the database the server lost connection"
print(get_num_characters(text))


def sort_on(servers):
    return servers["response_time"]

def get_sorted():   
    servers = [
        {"name": "web-01", "response_time": 230},
        {"name": "db-01", "response_time": 45},
        {"name": "cache-01", "response_time": 180},
        {"name": "api-01", "response_time": 90},
    ]
    servers.sort(reverse=False, key=sort_on)
    return servers

servers = get_sorted()
for server in servers:
    print(f"{server['name']}: {server['response_time']}ms")

def sort_on(dict1):
    return dict1["counts"]

def get_sorted(dict1):
    tlist = []
    for words, counts in dict1.items():
        tlist.append({"words": words, "counts": counts})
    tlist.sort(reverse=True, key=sort_on)
    return tlist

text1 = "the server crashed because the database the server lost connection"
word_counts = get_num_characters(text1)
sorted_words = get_sorted(word_counts)
for item in sorted_words:
    print(f"{item['words']}: {item['counts']}")