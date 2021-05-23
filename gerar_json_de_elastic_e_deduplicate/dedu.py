#!/usr/local/bin/python3
import hashlib
from elasticsearch import Elasticsearch
es = Elasticsearch(["192.168.10.190:9200"])
dict_of_duplicate_docs = {}
# A linha a seguir define os campos que serão
# usado para determinar se um documento é duplicado
keys_to_include_in_hash = ["minute", "contact"]
# Processar documentos retornados pela pesquisa/scroll atual

'2,837,048'
class Values:
    def __init__(self):
        self.duplicados = []
val = Values() 

def populate_dict_of_duplicate_docs(hits):
    # print(len(hits))

    for item in hits:
        combined_key = ""
        for mykey in keys_to_include_in_hash:
            combined_key += str(item['_source']['doc'][mykey])
        # print(combined_key)
        # print(item)
        # input()

        # print(item['_source']['doc']['id_msg'],item['_source']['doc']['id_chat'])
        # print(item)
        # input()
        if not [item['_source']['doc']['contact'],item['_source']['doc']['minute']] in val.duplicados:
            val.duplicados.append([item['_source']['doc']['contact'],item['_source']['doc']['minute']])
        else:
            # input(combined_key)

            _id = item["_id"]
            print(_id)

            # input(_id)
            hashval = hashlib.md5(combined_key.encode('utf-8')).digest()
            # Se o hashval for novo, criaremos uma nova chave
            # no dict_of_duplicate_docs, ao qual será
            # atribuído o valor de uma matriz vazia.
            # Em seguida, colocamos o _id imediatamente na matriz.
            # Se o hashval já existir, então
            # apenas colocaremos o novo _id na matriz existente
            dict_of_duplicate_docs.setdefault(hashval, []).append(_id)
# Faça um loop em todos os documentos no índice e preencha a
# estrutura de dados do dict_of_duplicate_docs.
def scroll_over_all_docs():
        # "query" : {
        # "filtered" : {
        #     "query":   { "match": { "tweet": "manage text search" }},
        #     "filter" : { "term" : { "user_id" : 2 }}
    # data = es.search(index="new_base_whats", scroll='1m',  body={"size":100, "query": {"match_all": {}},"filtered" : { "filter" : { "doc.month" : { "month" : 5 }}}})
    # data = es.search(index="new_base_whats", scroll='1m',  body={"size":100, "query": {"match_all": {}}, "filter" : { "doc.month" : { "month" : 5 }}})
    # data = es.search(index="new_base_whats", scroll='1m',  body={"size":100, "query": {"bool": { "must": [{"match": {"month": 5}}]}}})
    # data = es.search(index="new_base_whats", scroll='5m',  body={"size":200, "query": {"match_all": {}}, "sort" : [{"doc.month" : {"order" : "desc", "mode" : "max"}}]})
    # data = es.search(index="new_base_whats", scroll='1m',  body={"size":527, {"sort" : [  {"doc.Data": {"order" : "desc"}}  ]   }     })
    # data = es.search(index="new_base_whats", scroll='1m',    body={"size":527, {"sort" : [  {"doc.Data": {"order" : "desc"}}  ]   }     })
    data = es.search(index="new_base_whats", scroll='1m',  body={"size":17 ,"sort" : [  {"doc.Data": {"order" : "desc"}}  ]   })
    # es.search(index="new_base_whats", body={"query": {"prefix" : { "name" : "lu" }}})
    # es.search(index="new_base_whats", body={"query": {"prefix" : { "month" : "5" }}})


    # input(data)
    # print(data)
    # input()
    # Obtenha o ID do scroll
    sid = data['_scroll_id']
    scroll_size = len(data['hits']['hits'])
    # input(scroll_size)
    # Antes do scroll, processe o lote atual de ocorrências
    populate_dict_of_duplicate_docs(data['hits']['hits'])
    # while scroll_size > 8:
    while 0:
        data = es.scroll(scroll_id=sid, scroll='2m')
        # Processe o lote atual de ocorrências
        populate_dict_of_duplicate_docs(data['hits']['hits'])
        # Atualize o ID do scroll
        sid = data['_scroll_id']
        # Obtenha o número de resultados retornados no último scroll
        scroll_size = len(data['hits']['hits'])
def loop_over_hashes_and_remove_duplicates():
    # Pesquise o hash dos valores dos documentos para ver se algum
    # hash duplicado foi encontrado
    print('removendo...')
    print(len(dict_of_duplicate_docs.items()))
    print((dict_of_duplicate_docs.items()))
    for hashval, array_of_ids in dict_of_duplicate_docs.items():
      if len(array_of_ids) > 1:
        print("********** Duplicate docs hash=%s **********" % hashval)
        # Obtenha os documentos que foram mapeados para o hashval atual
        matching_docs = es.mget(index="new_base_whats4", doc_type="doc", body={"ids": array_of_ids})
        # print("len")
        # print(len(matching_docs))
        # input()
        for doc in matching_docs['docs']:
            # Neste exemplo, apenas imprimimos os documentos duplicados.
            # Este código poderia ser facilmente modificado para excluir duplicatas
            es.delete(index="new_base_whats" , id=doc['_id'])
            # es.delete(index=doc['new_base_whats4'], id=doc['_id'])
            # aqui em vez de imprimi-las
            print("delete doc=%s\n" % doc)
            # print("delete doc=%s\n" % doc['doc.message'] )
            # input()
      else: 
          es.delete(index="new_base_whats" , id=array_of_ids)
          print("delete doc=%s\n" % array_of_ids)
def main():
    scroll_over_all_docs()
    loop_over_hashes_and_remove_duplicates()
main()