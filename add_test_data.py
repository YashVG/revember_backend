
from firebase import db #imports firebase client




def add_test_data():
    doc_ref = db.collection(u'test').document(u'alovelace')
    doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
        })
    

add_test_data()

if __name__ == '__main__':
    add_test_data()

