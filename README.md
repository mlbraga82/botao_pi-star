# O que é?

  Programa para criação de um serviço para realizar as funções de Drop Call e Remove Static Group usando um botão físico inserido no hotspot do pi-star.

# Quando?

  Criado em 07/set/20 por PY7SLB (mlbraga82@gmail.com), dúvidas e sugestões podem entrar em contato.

# Como funciona?

  O programa é um script python que monitora o pino GPIO 10 que estará ligado a um botão físico, quando este botão é pressionado um script é acionado que irá identificar nos arquivos de LOG do pi-star qual o último TG que foi acionado e executará os comandos de drop QSO e Remove Static Group. Para isso é necessário que o hotspot esteja com o BM API cadastrado (verificar requisitos abaixo)
  
# Pra quê serve?

  Nas redes DMR é comum (em alguns Talkgroups) os usuários não deixarem um intervalo entre um cambio e outro, impedindo um operador de sair do grupo acionando o TG 4000 (disconnect). Para impedir que o usuário "fique preso" ao TG, é possível usar os comandos da Brandmeister para realizar o DROP QSO e Remove TG para sair de grupos estáticos. Este programa não substitui o TG 4000 (Disconnect) para TG dinâmicos (aqueles que você acessa usando o PTT), porém este programa dará a liberdade para acionar o TG 4000 do seu rádio mesmo que os usuários do TG ocupado estejam ainda transmitindo. Basta apertar o botão aguardar o contato ser interrompido e transmitir o TG4000 para desconectar.

# Ligações físicas:

Exemplo: (https://github.com/mlbraga82/botao_pi-star/wiki)
Testado no Raspbery Pi Zero
```
                 10k        SW
3.3V   o------/\/\/\/\-----/ __----
                                   |
GPIO10 o---------------------------
```
# Requisitos:

1) ativar o serviço Brandmeister API no hotspot
  https://news.brandmeister.network/introducing-user-api-keys/
2) baixar o pip3: 
  ```
  sudo apt install python3-pip
  ```
3) Instalar a bilbioteca do python RPi.GPIO
```
  pip3 install RPi.GPIO
  ```
4) Colocar os arquivos last_tg.py e botao_service.py no diretório /home/pi-star/
5) Colocar aquivo em botao.service em /lib/systemd/system/
6) Ativar o serviço usando os comandos
```
  sudo systemctl daemon-reload
  sudo systemctl enable botao.service
  sudo systemctl start botao.service
  sudo systemctl status botao.service
```
Se tudo funcionou corretamente não é necessário mais nenhuma intervenção. Seu hotspot pode reiniciar normalmente. Quando retornar irá executar o serviço botao.service de forma automática.
