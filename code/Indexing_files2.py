from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT #predefined types of fields
import os.path
from os.path import isfile, join
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.qparser import QueryParser


#definition of the schema (fields that the index is going to have)
schema = Schema(title=TEXT(stored=True), content=TEXT,
                path=ID(stored=True), tags=KEYWORD, icon=STORED)

#path where the index is going to be created
path_ix = '/home/gerardo/Documents/Mios/Docsmios/DCC/IIMAS_Cursos_IVMR/Rosa_Espino/indice'

#path where the files exist
path_files = '/home/gerardo/Documents/Mios/Docsmios/DCC/IIMAS_Cursos_IVMR/Rosa_Espino/Poemas_index/'

if not os.path.exists(path_ix):
    os.mkdir(path_ix)

#creation of the index, it should be done only once or it will clear the contents of the index
ix = create_in(path_ix, schema)


#open the index created in the path specified
ix = open_dir(path_ix)

#This locks the index for writing
writer = ix.writer()

files = os.listdir(path_files)

for f in files:
#variable with the files paths (path_files) and names (f)
    files_x = path_files + f
#    file2 = "/home/gerardo/Documents/Mios/Docsmios/DCC/IIMAS_Cursos_IVMR/Rosa_Espino/Poemas/1.txt"
    if os.path.isfile(files_x):
        print(f)
        file1 = open(files_x, 'r')
        content1 = file1.read()
        file1.close()
    with open(files_x,'r') as f:
        line = f.readline()
        line = line.rstrip('\n')
        print(line.rstrip('\n'))
        print
        lines = f.readlines()
 #       for line in lines:
 #           print(line.rstrip('\n'))
        f.close()

    writer.add_document(title=line, content=content1,
                    path=u"/c", tags=u"Rosa Espino")

writer.commit()




#for f in files:
#variable with the files paths (path_files) and names (f)
#    files_x = path_files + f
#    if os.path.isfile(files_x):
#        print(f)


#file that is going to be read and inserted in the index
#file1=open(files_x,'r')
#content1 =file1.read()
#file1.close()
#print(content1)


#examples
#writer.add_document(title=u"My document", content=u"This is my document!",
#                    path=u"/a", tags=u"first short", icon=u"/icons/star.png")
#writer.add_document(title=u"Second try", content=u"This is the second example.",
#                    path=u"/b", tags=u"second short", icon=u"/icons/sheep.png")
#writer.add_document(title=u"Third time's the charm", content=u"Examples are many.",
#                    path=u"/c", tags=u"short", icon=u"/icons/book.png")

#Adding the document to the index

#To search in the index
searcher = ix.searcher()

#parser = QueryParser("content", ix.schema)
#myquery = parser.parse("This is")

#On what field is goingo to be done the search, in this case in "content"
qp = QueryParser("content", schema=ix.schema)
#The text to search
A = input("\nIntroduzca la frase a buscar: ")

#q = qp.parse(u"que lucis ese llanto")
print('\n')
print (A)
q = qp.parse(A)



with ix.searcher() as s:
    results = s.search(q,terms=True)

#results = searcher.search(myquery)



#print("How many results:",len(results))
#print("resultados", results)

# Was this results object created with terms=True?
if results.has_matched_terms():
    # What terms matched in the results?
    print("Terms matched in the results", results.matched_terms())

for hit in results:
  stored_fields = searcher.stored_fields(hit.docnum)
  print("\n")
  print(stored_fields)
  print("The score: ", hit.score)
  print("The rank: ", hit.rank)
  print("The document number:", hit.docnum)
  print("Terms matched in hit", hit.matched_terms())


    # What terms matched in each hit?
 #   for hit in results:
 #       print("Terms matched in each hit", hit.matched_terms())

#print(results[0])
