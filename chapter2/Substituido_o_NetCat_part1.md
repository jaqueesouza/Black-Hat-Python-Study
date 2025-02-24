Substituindo o NetCat part. 1

Desta vez escolhi algo diferente, ao invés de postar o código aqui irei explicar partes dele que parecem, ou são, avançados para iniciantes em python. Isso não substitui o livro, lá possui explicações sobre o que está acontecendo, mas o autor pressupõe que você conhece a linguagem python e passa direto por algumas coisas. Vamos lá!

No python nós começamos importando as bibliotecas que vamos utilizar, para isso temos o comando “import” seguido da biblioteca que queremos, neste caso são essas:

--  

  
import argparse - Para processar argumentos passados na linha de comando.  

import socket - Permite a criação e gerenciamento de conexões de rede.  

import shlex - Facilita dividir strings em tokens, útil para interpretar comandos.  

import subprocess - Executa novos processos e comandos no SO.  

import sys - fornece acesso a variáveis e funções relacionadas ao interpretador python.  

import textwrap - auxilia na formatação de texto em blocos ajustáveis.  

import threading - suporte a execução de múltiplos threads (tarefas simultâneas).   

--  


def execute (cmd): - Aqui o “execute” é como dizer ao computador “faça isso para mim”.  

cmd = cmd.strip() - Tira os espaços extras da frente e do final do comando.  

if not cmd: - Se não houver comando nenhum, a função não fará nada.  

--  


output = suprocess.acheck_output(shlex.split(cmd) - Pede ao computador para executar o comando e guarda o resultado.  

Return output.decode() - Devolve o resultado como uma mensagem que podemos entender.  


Seguindo o livro tem explicações sobre o “execute”, “subprocess” e “check_output”.
