import json
import pickle


__data_columns = None
__model = None

def get_col_names():
    pass


def load_saved_artefacts():
    print("loading saved artefacts ... start")
    global __data_columns

    with open("./artefacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']

    with open("./artefacts/hiring.pkl", 'rb') as f:
        __model = pickle.load(f)
    print("loading artefacts .... done")



if __name__ == '__main__':
    load_saved_artefacts()
    print(get_col_names())