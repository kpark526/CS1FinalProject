# CS1FinalProject

Solitaire final project by Kelley and Jude.

This solitaire project has a menu for you to choose from two modes of solitaire.
To start a game, download all the files included. Then run solitaire_menu.py. You can also run the file for the mode you want directly.

Freestyle Solitaire:
- Starts off with a shuffled deck of cards.
- All movements are up to the player, and can move cards anywhere.
- This allows for unlimited freedom, and a full game of solitaire can be played, but a vast majority of the actions are decided by the player.
- Restrictions
	- Could not make separate card objects for each picked up card. When dragging a card the last place the card was is kept on the screen.

"Classic" Solitaire:
- Starts off with a shuffled deck of cards and a premade board state.
- The gameplay area does have the classic solitaire layout (that is, *there are* cards underneath), but we were unable to implement proper cascading on the piles
- Basic solitaire rules implemented
- Restrictions
	- Cannot move piles at a time
	- Cannot view the stack created with revealed cards


Credits:
- Card images were pulled from the internet
- Menu Theme : Main Theme from Fruit Box by GameSaien
- Easy/Hard Solitaire Theme : Title Theme from Super Mario Maker by Nintendo

- If you have problems with the music/music not working, comment out the three lines for the music loading in each file
