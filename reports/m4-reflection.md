Implemented/Refined since Milestone 3:
- Added memory caching to speed up the app
- Use a binary format to load data faster
- Created a popout for our about section instead of an expanding section in the control panel
- Changed scatterplot to filter the generations shown based on the global filter
- Changed control panel filters to apply to all charts
- Change search bar to not show Pikachu selected (instead show a prompt to type the name of a pokemon)
- Set favicon and title
- Updated README 
- Updated gif
- Changed overall layout code to separate plots into two rows first (rather than two columns) to try and fix chart height alignment

Done differently from our initial proposal/sketch:
- The chart layout was adjusted slightly to have the two plots with user chosen axes in the top row. This was done so the user won’t have to move their cursor around the screen as much, more convenient as the dropdown options are closer together. 
- The chart comparing the effectiveness of other pokemon types against your chosen pokemon was changed to a bar plot rather than a heatmap. This was done because we thought it would be more intuitive for the user to understand.
- General color theme choices are different from our initial sketch. Adding colouring for each type in two of the plots made them more cohesive and easier to view for the user comparing different pokemon types.
- Overall we have fewer sliding filters in the main control panel. In our initial sketch we also had Base Happiness, Egg Step, Capture Rate, Height and Weight which are now not included in the control panel. We decided to remove these to not clutter the control too much and they are not as likely to be used by users when choosing or exploring their pokemon attributes.

Known bugs/issues:
- Certain Pokemon with regional forms (eg. Raticate/Alolan Raticate) have inaccurate representations in the dataset causing the dashboard to display incorrect information

Deviations from 531 effective visualizations
- Our plots follow 531 best practices, with an exception of our scatterplot, which tends to overplot depending on the filters the user chooses. If very few filters are altered and all or most Pokemon are included in the chart it is a lot of points on the chart, and is overplotting.

Dashboard Strengths:
- Ability to compare many different stats in one place.
- Ability for the user to change the chart axes to statistics of their preference, tailoring the experience for what they’d like to explore.
- Overall visually appealing with the Pokemon sprites included on the left panel, as well as plotted on 2 of the charts.
Dashboard Limitations:
- The data is static, so it will not be updated in real time if new Pokemon are created or added. 
- Currently no option to select and compare more than one pokemon at once
Potential Future Improvements:
- Adding the ability to select and then compare 2-3 pokemon at once, (rather than selecting one and comparing it to all Pokemon).
