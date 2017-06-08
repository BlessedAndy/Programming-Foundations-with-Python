'''
Created on Oct 14, 2016

@author: Andy Zhang
'''

print 'beging to get data...'
collectionSize = Collection.Size()
searchTermRec = DataManager.NewDataRecord()
terms = []


for recNum in range(collectionSize, 0, -1):
    Collection.GetRecord(searchTermRec, recNum)
    searchTerm = searchTermRec.GetField(u'Term')
    terms.append(searchTerm)
    Collection.DeleteRecord(searchTermRec)

DataManager.DeleteDataRecord(searchTermRec)

print 'total %d term to search.'%(collectionSize)

for term in terms:    
    newRecord = DataManager.NewDataRecord(1)
    newRecord.SetField(u'DESCRIPTION',term)
    Collection.AddRecord(newrecord)
    del newRecord
    
print 'done'
    