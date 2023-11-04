# X_Y_online
- "X_Y_online" - игра "Крестики-нолики" онлайн.
- X - крестик; Y - нолик
- Как запустить(под linux)?
  - ```
    git clone https://github.com/evgeniyARCH/X_Y_online.git
  - Server:
  - ```
    python3 /home/$USER/X_Y_online/server_game.py
  - x_client:
  - ```
    python3 /home/$USER/X_Y_online/x_client.py
  - y_client:
  - ```
    python3 /home/$USER/X_Y_online/y_client.py
- Суть
  - Каждый ход у игрока запрашивается номер поля, куда ходить
  - игроки ходят по очереди(как в оригинальной игре)
  - Способ победы такой же, как в настоящей игре "Крестики-нолики"
- Как играть по онлайну?
  - Запускаем на основном ПК Server
  - Подключаем к серверу(основному ПК) 2 устройства по ssh
  - На одном запускаем x_client
  - На другом - y_client
  - Играем
