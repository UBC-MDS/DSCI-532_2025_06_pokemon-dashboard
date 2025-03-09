# Milestone 3 Reflection

## Implemented Features

- Add boxes around the dashboard components for cleaner visualization
- Add background colour to global option sidebar to make it stand out from the rest of the dashboard
- Change placeholder text in "Type 1" and "Type 2" dropdowns for cleaner selection
- Allow case-insensitive search in the Pokemon search bar
- Add text "Comparison Filter" to make it more clear what the additional filters are supposed to do
- Move dashboard components so that the components with inputs are near to each other
- Rename Pokemon type weaknesses to human readable format
- Match colours of the Pokemon type weaknesses and Pokemon stat distributions to the Pokemon type colours
- Move "About" section to a popup
- Break code into multiple files
- Implement a dedicated display showing detailed stats for the selected Pokémon

## Features Not Yet Implemented

- Apply global filters to all charts
- Add adjustable y-axis in stat distribution boxplot to allow visualization of both Type 1 and Type 2 on y-axis
- Automate downloading the dataset from Kaggle

## Differences from Proposal/Sketch

- No significant deviations from the proposal that were not already mentioned in Milestone 2 Reflection

## Known Corner Cases/Bugs

- Changing the width of the browser window can cause some visual issues, such as the selected Pokemon card extending beyond the width of the sidebar
- Certain Pokemon with regional forms (eg. Raticate/Alolan Raticate) have inaccurate representations in the dataset causing the dashboard to display incorrect information

## Dashboard Strengths

- The dashboard is visually appealing and provides several useful input features and filters for exploring Pokemon data, and custom chart axis inputs

## Dashboard Limitations

- The global filters currently do not apply to all charts
- The data is a static copy so it cannot be updated in real time

## Future Improvements

- Implement "Features Not Yet Implemented"
- Implement feedback from classmates and previous deliverables

## Incorporating Inspiration from Peers (Challenging)

- We were facing challenges with our global options sidebar, specifically the Type 1 and Type 2 selection dropdowns. Some dashboards from our peers (eg. "CAN-US Trade Relations Dashboard") included a sidebar with dropdowns stacked on top of each other. We decided to implement a similar layout for our dashboard as we found it visually appealing and easier to navigate
