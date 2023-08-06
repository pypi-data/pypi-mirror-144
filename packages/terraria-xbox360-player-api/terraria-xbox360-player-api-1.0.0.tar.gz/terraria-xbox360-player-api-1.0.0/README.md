# terraria xbox360 player API

API for reading and modifying xbox 360 terraria player files.

## Examples

Change player max life to 300
```python
>>> from terraria_xbox360_player_api import terraria_xbox360_player_api
>>> player = terraria_xbox360_player_api.TerrariaPlayerXbox360("PLAYER1.PLR")
>>> player.max_life = 300
>>> player.write_to_file("PLAYER1.PLR")
```

Set 999 dirt items to first inventory slot
```python
>>> from terraria_xbox360_player_api import terraria_xbox360_player_api
>>> player = terraria_xbox360_player_api.TerrariaPlayerXbox360("PLAYER1.PLR")
>>> player.max_life = player.inventory[0][0] = player.Item(2, 999, 0)
>>> player.write_to_file("PLAYER1.PLR")
```

Read player name
```python
>>> from terraria_xbox360_player_api import terraria_xbox360_player_api
>>> import terraria_xbox360_player_api
>>> terraria_xbox360_player_api.TerrariaPlayerXbox360("PLAYER1.PLR").name
'test_plr'
```

## Dependencies

[bitarray](https://github.com/ilanschnell/bitarray)

## License

[GPL v3](LICENSE) © Filip K.
