from models import Pessoas, db_session

#Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Lima', idade=20)
    print(pessoa)
    db_session.add(pessoa)
    db_session.commit()

#Realizada consulta na tabela pessoa
def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)

    pessoa = Pessoas.query.filter_by(nome='Joao').first()
    print(pessoa.idade)

#Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lima').first()
    pessoa.nome = 'Vitor'
    pessoa.save()

#Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lima').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #consulta()
    #altera_pessoa()
    #exclui_pessoa()
    pass