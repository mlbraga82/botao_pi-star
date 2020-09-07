Programa para criação de um serviço para realizar as funções de Drop Call e Remove Static Group usando um botão físico inserido no hotspot do pi-star.

Ligações físicas:
Raspbery Pi Zero

                 10k        SW
3.3V   o------/\/\/\/\-----/ __----
                                  |
GPIO10 o--------------------------

Requisitos:
1) baixar o pip3: 
  sudo apt install python3-pip
2) Instalar a bilbioteca do python RPi.GPIO
  pip3 install RPi.GPIO
3) Colocar os arquivos last_tg.py e botao_service.py no diretório /home/pi-star/
4) Colocar aquivo em botao.service em /lib/systemd/system/
5) Ativar o serviço usando os comandos
  sudo systemctl daemon-reload
  sudo systemctl enable botao.service
  sudo systemctl start botao.service
  sudo systemctl status botao.service


