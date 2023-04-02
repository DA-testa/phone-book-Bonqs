def hash_phone_number(number):
    leng = len(number) // 2
    left_half = number[:leng]
    right_half = number[leng:]
    value = int(left_half) * int(right_half) % 10
    return value

class Query:
    def __init__(self, query):
        self.type, self.number = query[0], int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for _ in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result, contacts = [], {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            contacts.pop(cur_query.number, None)
        else:
            response = contacts.get(cur_query.number, 'not found')
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
