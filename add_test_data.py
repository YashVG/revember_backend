
from firebase import db #imports firebase client

data = {
    u'name': u'Los Angeles',
    u'state': u'CA',
    u'country': u'USA'
}


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

