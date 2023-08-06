# Welcome to czapi
> A basic API for scraping curling boxscores off of the popular <a href='https://www.curlingzone.com'>CurlingZone</a> website. 


## Install

```
pip install czapi
```

## How to use

```python
import czapi.api as api
```

### General Information

Event & game information can be accessed in two ways. 

1. Using the game id (cz_game_id) as provided by CurlingZone. 
2. Using the event id (cz_event_id) as provided by CurlingZone. 
    * If using the event id for boxscores, the draw id (cz_draw_id) and game number (game_number) must also be provided.

### Event Details

Here is an example of getting event details using both methods mentioned above.

```python
event_name = api.get_event_name(cz_event_id = 6100)
event_name
```




    'Curling Night in America'



```python
event_date = api.get_event_date(cz_game_id = 253869)
event_date
```




    'Aug 22 - 24, 2019'



### Boxscore

A boxscore is returned as a dictionary of team names, game information dictionary key, value pairs. 

Each game information dictionary contains: 
* 'href' key with a corresponding string value of CurlingZone IDs identifying the team.
* 'hammer' key with corresponding boolean value of whether or not that team started the game with hammer.
* 'score' key with corresponding list of string value of end-by-end results for that team.
* 'date' key with corresponding string value of the date of the event.
* 'event' key with corresponding string value of the name of the event.
* 'hash' key with corresponding SHA256 hash of the entire boxscore. 

Here is an example of getting the boxscore information using only the game id. 

```python
game_result_dict = api.get_full_boxscore(cz_game_id = 271145)
game_result_dict
```




    {'Wayne Tuck Jr.': {'href': 'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1',
      'hammer': True,
      'score': ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'],
      'finalscore': '5',
      'date': 'Jan 17 - 19, 2020',
      'event': 'Ontario Tankard - Open Qualifier',
      'draw': 'Not supported for boxscore page.',
      'hash': '944b4b512a0b43e5d8dc569a6483863108d16dcc659eec5d73c58a252eed5507'},
     'Matthew Hall': {'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      'hammer': False,
      'score': ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'],
      'finalscore': '7',
      'date': 'Jan 17 - 19, 2020',
      'event': 'Ontario Tankard - Open Qualifier',
      'draw': 'Not supported for boxscore page.',
      'hash': '944b4b512a0b43e5d8dc569a6483863108d16dcc659eec5d73c58a252eed5507'}}



> Output above should match the results from [here](https://curlingzone.com/game.php?1=1&showgameid=271145#1).

Here is an example of getting the boxscore information using the event id, draw id and game number. 

```python
another_game_result_dict = api.get_full_boxscore(cz_event_id = 6100, cz_draw_id = 3, game_number = 1)
another_game_result_dict
```




    {'Joel Retornaz': {'href': 'event.php?view=Team&eventid=6100&teamid=136100&profileid=12467#1',
      'hammer': False,
      'score': ['0', '1', '0', '1', '1', '0', '2', '0'],
      'finalscore': '5',
      'date': 'Aug 22 - 24, 2019',
      'event': 'Curling Night in America',
      'draw': 'Draw: 3',
      'hash': 'a30c99626ce44a68a8d3c48c5f8f6b86eea054bef1170c591c1efebebf61f549'},
     'John Shuster': {'href': 'event.php?view=Team&eventid=6100&teamid=136086&profileid=12473#1',
      'hammer': True,
      'score': ['1', '0', '1', '0', '0', '2', '0', '3'],
      'finalscore': '7',
      'date': 'Aug 22 - 24, 2019',
      'event': 'Curling Night in America',
      'draw': 'Draw: 3',
      'hash': 'a30c99626ce44a68a8d3c48c5f8f6b86eea054bef1170c591c1efebebf61f549'}}



> Output above should match the results from [here](https://www.curlingzone.com/event.php?eventid=6100&view=Scores&showdrawid=3#1).

## About czapi
czapi is a Python library for scraping curling linescores.
