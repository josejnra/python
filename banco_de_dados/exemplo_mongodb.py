from pymongo import MongoClient
import datetime

# Estabelecer a conexão com o Banco de Dados
connection = MongoClient("localhost", 27017)

"""
 Uma única instância do MongoDB pode suportar diversos bancos de dados.
 Abaixo é criado o banco de dados cadastrodb
"""
db = connection.cadastrodb


"""
 Coleção é um grupo de documentos armazenados no MongoDB.
 (relativamente parecido com o conceito de tabelas em bancos relacionais).
 A coleção só será efetivamente criada quando for inserido dados nela.
 A coleção cadastrodb não será criada pois não é salvo nada nela. 
"""
collection = db.cadastrodb


"""
 Dados no MongoDB são representados (e armazenados) usando documentos JSON.
 Com o PyMongo é usado dicionários para representar documentos.
"""
post1 = {
    "codigo": "ID-9987725",
    "prod_name": "Geladeira",
    "marcas": ["brastemp", "consul", "eletrolux"],
    "data_cadastro": datetime.datetime.utcnow(),
}


# inserir documento na coleção posts
collection = db.posts

post_id = collection.insert_one(post1)
print(post_id.inserted_id)

"""
 Quando um documento é inserido uma chave especial, "_id", é adicionada
 automaticamente se o documento ainda não contém uma chave "_id".
"""
print(post_id)

post2 = {
    "codigo": "ID-2209876",
    "prod_name": "Televisor",
    "marcas": ["samsung", "panasonic", "lg"],
    "data_cadastro": datetime.datetime.utcnow(),
}

collection = db.posts

post_id = collection.insert_one(post2).inserted_id

print(collection.find_one({"prod_name": "Televisor"}))

"""
 A função find() retorna um cursor e assim pode-se então navegar pelos dados
"""
print("\n\n")
for post in collection.find():
    print(post)


# nome do banco
print(db.name)

# Listando as coleções disponíveis
print(db.collection_names())

print(dir(MongoClient))
