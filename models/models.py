from config import db
from flask_login import UserMixin
from datetime import datetime
from pytz import timezone



class Ops_visual(db.Model):
    __tablename__='ops_visual'

    id = db.Column(db.Integer, primary_key=True)   
    numero_op_visual = db.Column(db.String(50))
    piv = db.Column(db.Integer)
    situação = db.Column(db.String(50))
    item = db.Column(db.String(50))
    descrição = db.Column(db.String(255))
    quantidade = db.Column(db.Integer)
    peso_enviado = db.Column(db.Integer)
    peso_retornado = db.Column(db.Integer)
    fino_enviado = db.Column(db.Integer)
    fino_retornado = db.Column(db.Integer)
    data_abertura = db.Column(db.String(255))
    hora_abertura = db.Column(db.String(255))
    setor = db.Column(db.String(255))
    operador = db.Column(db.String(255))



    def __init__(self, numero_op_visual, piv, situação, item, descrição, quantidade, peso_enviado, peso_retornado, fino_enviado, fino_retornado, data_abertura, hora_abertura, setor = setor, operador = operador):
        
        self.numero_op_visual = numero_op_visual
        self.piv = piv
        self.situação = situação
        self.item = item
        self.descrição = descrição
        self.quantidade = quantidade
        self.peso_enviado = peso_enviado
        self.peso_retornado = peso_retornado
        self.fino_enviado = fino_enviado
        self.fino_retornado = fino_retornado
        self.data_abertura = data_abertura
        self.hora_abertura = hora_abertura
        self.setor = setor
        self.operador = operador

    def __repr__(self):
        return 'Ops: {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}' .format(self.id, self.numero_op_visual, self.piv, self.situação, self.item, self.descrição, 
                                                                    self.quantidade, self.peso_enviado, self.peso_retornado, self.fino_enviado, self.fino_retornado, self.data_abertura, self.setor, self.operador)


class Lote_visual(db.Model):
    __tablename__='lote_visual'

    id = db.Column(db.Integer, primary_key=True)
    referencia = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    item = db.Column(db.String(50), nullable=False)
    lote_visual = db.Column(db.String(50), nullable=False)
    numero_lote = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    fino = db.Column(db.Integer)
    local = db.Column(db.String(50), nullable=False)
    obs = db.Column(db.String(250))
    data_criacao = db.Column(db.String(250), nullable=False)
    processado_op = db.Column(db.Integer)
    quant_inicial = db.Column(db.Integer, nullable=False)
    
    def __init__(self, referencia, tipo, item, lote_visual, numero_lote, quantidade, peso, fino, local, obs, data_criacao, processado_op, quant_inicial):
        
        self.referencia = referencia
        self.tipo = tipo
        self.item = item
        self.lote_visual = lote_visual
        self.numero_lote = numero_lote
        self.quantidade = quantidade
        self.peso = peso
        self.fino = fino
        self.local = local
        self.obs = obs
        self.data_criacao = data_criacao
        self.processado_op = processado_op
        self.quant_inicial = quant_inicial
        

    def __repr__(self):
        return f"Lote_visual(id={self.id}, referencia={self.referencia}, tipo={self.tipo},  item={self.item}, lote_visual={self.lote_visual}, numero_lote={self.numero_lote}, quantidade={self.quantidade}, peso={self.peso}, fino = {self.fino}, local = {self.local}, obs = {self.obs}, data_criacao = {self.data_criacao}, processado_op = {self.processado_op}, quant_inicial = {self.quant_inicial})"

class Estrutura_op(db.Model):
    __tablename__='estrutura_op'

    id = db.Column(db.Integer, primary_key=True)
    op_referencia = db.Column(db.Integer, nullable=False)
    tipo_mov = db.Column(db.String(50)) 
    item_estrutura = db.Column(db.String(50), unique=True)
    descricao_item = db.Column(db.String(255))
    quantidade_item = db.Column(db.Float)
    peso = db.Column(db.Float)
    fino = db.Column(db.Float)
    

    
    def __init__(self, op_referencia, tipo_mov, item_estrutura, descricao_item, 
                quantidade_item, peso, fino):  

        self.op_referencia = op_referencia
        self.tipo_mov = tipo_mov
        self.item_estrutura = item_estrutura
        self.descricao_item = descricao_item
        self.quantidade_item = quantidade_item
        self.peso = peso
        self.fino = fino
       

    def __repr__(self):
        return 'estrutura_op: {} - {} - {} - {} - {} - {} - {}' .format(self.op_referencia, self.tipo_mov, self.item_estrutura, self.descricao_item, self.quantidade_item, self.peso, self.fino)


class Lotes_mov_op(db.Model):
    __tablename__='lotes_mov_op'

    id = db.Column(db.Integer, primary_key=True)
    referencia = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    item = db.Column(db.String(50), nullable=False)
    lote_visual = db.Column(db.String(50), nullable=False)
    numero_lote = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    fino = db.Column(db.Integer)
    data_mov = db.Column(db.String(250), nullable=False)
    id_lote = db.Column(db.Integer, nullable=False)
    
    def __init__(self, referencia, tipo, item, lote_visual, numero_lote, quantidade, peso, fino, data_mov, id_lote):
        
        self.referencia = referencia
        self.tipo = tipo
        self.item = item
        self.lote_visual = lote_visual
        self.numero_lote = numero_lote
        self.quantidade = quantidade
        self.peso = peso
        self.fino = fino
        self.data_mov = data_mov
        self.id_lote = id_lote
        

    def __repr__(self):
        return f"Lote_visual(id={self.id}, referencia={self.referencia}, tipo={self.tipo},  item={self.item}, lote_visual={self.lote_visual}, numero_lote={self.numero_lote}, quantidade={self.quantidade}, peso={self.peso}, fino = {self.fino}, data_mov = {self.data_mov}, id_lote = {self.id_lote})"




class Sequencia_op(db.Model):
    __tablename__='sequencia_op'
    
    tabela_campo = db.Column(db.String(50), primary_key=True)
    valor = db.Column(db.Integer, nullable=False)
    valor_anterior = db.Column(db.Integer, nullable=False)

    def __init__(self, tabela_campo, valor, valor_anterior):

        self.tabela_campo = tabela_campo
        self.valor = valor
        self.valor_anterior = valor_anterior
    
    def __repr__(self):
        return 'sequencia: {} - {} - {}' .format(self.tabela_campo, self.valor, self.valor_anterior) 


class Sequencia_lote(db.Model):
    __tablename__='sequencia_lote'
    
    op_visual = db.Column(db.String(50), primary_key=True)
    valor = db.Column(db.Integer, nullable=False)
    valor_anterior = db.Column(db.Integer, nullable=False)

    def __init__(self, op_visual, valor, valor_anterior):

        self.op_visual = op_visual
        self.valor = valor
        self.valor_anterior = valor_anterior
    
    def __repr__(self):
        return 'sequencia: {} - {} - {}' .format(self.op_visual, self.valor, self.valor_anterior) 

class Config_Visual(db.Model):
    __tablename__='config_visual'
    
    config = db.Column(db.String(50), primary_key=True)
    info = db.Column(db.String(50), nullable=False)
    
    def __init__(self, config, info):

        self.config = config
        self.info = info
        
    def __repr__(self):
        return 'sequencia: {} - {} - {}' .format(self.config, self.info) 



class Movimentos_estoque(db.Model):
    __tablename__='Movimentos_estoque'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(50))
    tipo = db.Column(db.String(50))
    lote_visual = db.Column(db.String(50))
    referencia = db.Column(db.Integer)
    quantidade = db.Column(db.Integer)
    local = db.Column(db.String(50))
    obs = db.Column(db.String(250))
    data_movimento = db.Column(db.String(255))
    hora_movimento = db.Column(db.String(255))
    usuario = db.Column(db.String(90))
    id_movest = db.Column(db.BigInteger)
    id_ajuste = db.Column(db.BigInteger)
    status_mov = db.Column(db.String(50))
    id_lote = db.Column(db.Integer)
    

    def __init__(self, item, tipo, lote_visual, referencia,
                 quantidade, local, obs,  data_movimento, hora_movimento,
                 usuario, id_movest, id_ajuste, status_mov, id_lote):  

        self.item = item
        self.tipo = tipo
        self.lote_visual = lote_visual
        self.referencia = referencia
        self.quantidade = quantidade
        self.local = local
        self.obs = obs
        self.data_movimento = data_movimento
        self.hora_movimento = hora_movimento
        self.usuario = usuario
        self.id_movest = id_movest
        self.id_ajuste = id_ajuste
        self.status_mov = status_mov
        self.id_lote = id_lote


    def __repr__(self):
        return 'Movimentos_estoque: {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}' .format(self.id, self.item, self.tipo, self.lote_visual,self.referencia, 
                self.quantidade, self.local, self.obs, self.data_movimento, self.hora_movimento, self.usuario, self.id_movest, self.id_ajuste, self.status_mov, self.id_lote)



class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

        
    def __repr__(self):
        return "<User %r>" % self.email


