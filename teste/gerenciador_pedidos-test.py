import sys
import os
import pytest

caminho_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(caminho_raiz)

from gerenciador_pedidos import GerenciadorPedidos

def test_adicionar_item():
    gerenciador = GerenciadorPedidos()
    gerenciador.adicionar_item("produto1", 2, 10.0)
    gerenciador.adicionar_item("produto2", 1, 20.0)
    
    assert len(gerenciador.itens) == 2
    assert gerenciador.itens == [['produto1', '2', '10.0'], ['produto2', '1', '20.0']]
   
def test_processar_pedido_cliente_sem_nome():
    gerenciador = GerenciadorPedidos()
    resultado = gerenciador.processar_pedido("", "exemplo", "comum", "pix", 0, "Rua A", "123", "Cidade X", "PE", "123457")

    assert resultado == 'ERRO: cliente sem nome'

def test_processar_pedido_email_invalido():
    gerenciador = GerenciadorPedidos()
    resultado = gerenciador.processar_pedido("Paula", "exemplo", "comum", "pix", 0, "Rua A", "123", "Cidade X", "PE", "123457")

    assert resultado == 'ERRO: email invalido'





