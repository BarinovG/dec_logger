from app.decorator_for_logs import logger_to


@logger_to('test1.json')
def iqwe(x, y, c, a=0, b=0):
    return x + y + c + a + b


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': [],
}


@logger_to('test1.json')
def show_list(doc_list, dir_dict):
    res = []
    for info_doc in doc_list:
        res.append(f'{info_doc["type"]} "{info_doc["number"]}" "{info_doc["name"]}"')
    res2 = dir_dict
    return res, res2


if __name__ == '__main__':
    iqwe(3, 4, 2)
    show_list(documents, directories)
