# Trello
This is a small Python application that interacts with the Trello API. It pulls and parses all the cards in my 'Monthly Food Expenses' board then displays my monthly spending habits in a bar graph, tracks my yearly spending average and plots location frequency in a circular pie graph. It helps me visualize what months I'm spending more money and at what locations. This project can be adapted to any board that has numerical data that needs to be computed and displayed.



## Requirements:
Add a file, in the root directory called `keys.json` with your token and api_key in the following format:
token = alphanumeric
api_key = alphanumeric

### Python 2.x

- `pip install trollop`
- `pip install seaborn`
- `pip install matplotlib`

## Sample Trello Board with cards
![alt tag](https://raw.githubusercontent.com/211217613/trello-scraper/master/images/trello_screenshot.png)
## Sample Graph
![alt tag](https://raw.githubusercontent.com/211217613/trello-scraper/master/images/graph.png)


## Docker
- Need to fill this out. Run the app in a docker container

## TODO:
- Integrate testing framework
- Use algorithm to determine how much of a difference their is between names for clustering/binning
- Use VCR to reproduce API calls
- Parse name fields and graph in pie graph
- Integrate USD and MXN currencies
- Add line for yearly running average
- Add new year
- Migrate away from any print statements and use only logging
- Add list creation functionality to API wrapper (or make my own :) )
