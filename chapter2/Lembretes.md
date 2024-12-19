## Algumas coisas uteis de saber:

- socket =  ajuda a criar servidores e clientes em rede com Python.
- socket.AF_INET = indica que vai ser usado endereço IPv4.
- socket.SOCK_STREM = indica que o cliente é TCP.


TCP 
---
/Protocolo de Controle de Transmissão ou Transmission Control Protocol.
É um protocolo de comunicação que garante que os dados sejam transmitidos de forma segura e ordenada entre computadores, assegurando que os dados chegam completos, na ordem correta e sem erros. 
Ele é usado em serviços como websites, e-mails e downloads.



UDP
---
User Datagram Protocol
Diferente do TCP, o UDP não verifica se a mensagem chegou nem mantém controle de ordem, ele simplesmente envia os pacotes o mais rápido possível. 
O UDP é ideal para situações onde a velocidade é mais importante que a confiabilidade, como em chamadas de voz, streaming de vídeo e jogos online.



- connect() = "como UDP é um protocolo sem conexão não há chamada para  afunção antecipadamente".
- recvfrom() = recebe os dados do UDP de volta.
