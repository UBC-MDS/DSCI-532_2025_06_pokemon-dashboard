# Milestone 2 Reflection

## Implemented Features

We have successfully implemented several key features from our proposal, including:

- Search Bar: Allows users to search for their Pokémon of interest.
- Sliding Filters: Enables filtering Pokémon based on different attributes.
- Dropdowns: Enables filtering Pokémon based on generation and types.
- Scatter Plot: Users can interactively select both x- and y-axes for customized comparisons.
- Top 7 Bar Chart: Displays the top 7 pokemon base on filters and compare it to chosen pokemon, also with tooltip containing attributes and average stats.
- Boxplot of a Chosen Stat vs. Pokémon Type: Provides insights into the distribution of stats across Pokémon types.
- Effectivenes Barchar: Displays the effectivness of Pokemon types against each other.

## Features Not Yet Implemented & Known Issues

- Chosen Pokémon Status Card: We still need to implement a dedicated display showing detailed stats for the selected Pokémon.
- Adjustable Y-Axis for Boxplot: Currently, the boxplot only displays stats grouped by Type1. We plan to allow users to switch between Type1 and Type2 as the y-axis grouping variable.
- Case-Sensitive Search Issue: The search bar currently differentiates between uppercase and lowercase inputs. For example, searching for "bulbasaur" does not match "Bulbasaur." We plan to make this search case-insensitive.
- Dropdown multi-select format is still not the best, the auto adjustment ruins the experience of the user because of too many selected items.
- Automate downloading the dataset from Kaggle, rather than working with a static copy.
- Axis labels for the type disadvantage chart are not as descriptive as they could be. For example, changing the x-axis to have nominal labels (Immune, 0.25-resisted, 0.5-resisted, neutral, 2-effective, 4-effective) instead of numeric labels.
- A nice visual feature would be to colour-code plots based on typing. For example, the "top 7 pokemon" boxplot could be coloured by primary type, and the "type disadvantage" and "boxplot" plots could be coloured by type.

## Deviations from the Proposal

- Removal of Height, Weight, Capture Rate, Base Happiness, and Egg Steps: These attributes were removed from the dashboard due to increased complexity and limited practical insights for comparisons.
- Change from Heatmap to Bar Chart for Type Effectiveness: Initially, we proposed a heatmap to show type effectiveness, but we found that a bar chart is more intuitive and provides clearer comparisons.
- More Customization for Boxplot: We improved the boxplot to allow more flexibility in comparing stats, making it more useful for users analyzing Pokémon attributes.

## Reflection

### Strengths

- The dashboard currently provides a visually appealing and interactive way to explore Pokémon data.
- Interactive scatter plots and boxplots enhance usability by allowing custom comparisons.
- Filtering options make it easy to narrow down Pokémon based on user preferences.

### Limitations & Future Improvements

- Adding a Pokémon status card would enhance user experience by providing detailed information on a selected Pokémon.
- Improving search functionality by making it case-insensitive and potentially adding autocomplete.
- Refining visualization options, such as improving boxplot grouping and incorporating additional interactivity.
- Potentially reintroducing some removed attributes if we find a streamlined way to display them effectively.
- Adjust how the dropdown with multi-select works.

Overall, we are on track with our implementation and have made necessary adjustments based on feasibility and effectiveness. Our focus moving forward will be refining existing features and implementing missing elements to improve usability and clarity.
