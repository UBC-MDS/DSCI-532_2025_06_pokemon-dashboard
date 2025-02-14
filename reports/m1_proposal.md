# Pokémon Dashboard: Proposal

## Section 1: Motivation and Purpose

> In a few sentences, provide motivation for why you are creating a dashboard:
>
> - Who is your target audience, and what role are you embodying?
> - What is the problem the target audience is facing and why is it important to solve?
> - How can your dashboard assist in solving this problem for the intended target audience?

Our role: Data Analyst in Nintendo

Target audience: New Pokémon Player

With the rise of the Pokémon TCG and mobile games, more people are diving into the Pokémon world. However, newcomers often struggle to find Pokémon that match their interests due to the sheer number of options available. Understanding key attributes such as stats, types, abilities, and battle effectiveness is crucial for competitive players, while casual fans may enjoy exploring fun details like height, weight, and generation. To address this, we are propose building an interactive Pokémon Dashboard that allows users to explore Pokémon statistics with ease. Our dashboard will visualize key attributes, enable direct comparisons, and offer filtering and sorting options, making it easier for users to discover and analyze Pokémon in a way that suits their interests. Filtering by the generation they are playing will allow them to understand how a new pokemon compares amongst the other pokemons.

## Section 2: Description of the Data

> Include how many rows and columns there are in the dataset (that you plan to use). There should be a clear link to how the dataset and the variables you describe will help you solve your target audience's problem. Indicate at least one new variable that you are planning to derive/engineer for your visualizations. If there are no new variables to derive, indicate what additional information you would have liked to have in the dataset to better be able to answer your research questions (even if it is impossible for you to engineer it). If you are planning to visualize a lot of columns, provide a high level description of the variable types rather than listing every single column. For example, indicate that the dataset contains a variety of categorical variables for demographics and provide a brief list rather than describing every single variable. You may also want to consider visualizing a smaller set of variables given the short duration of this project. To be able to include this information you might wish to perform a brief exploratory data analysis for you to grasp what could be interesting variables to look at in your data. We will not be grading the EDA aspect, but include your EDA notebooks in the public GitHub repo, so that you have everything in one place.

We will be visualizing a dataset of 801 pokemons. Each pokemon has 41 variables that describe its characteristics, which we think could be useful for pokemon users to compare their different pokemons.

Pokemon variables 
Variables and descriptions are from: https://www.kaggle.com/datasets/rounakbanik/pokemon/data

- name: The English name of the Pokemon
- pokedex_number: The entry number of the Pokemon in the National Pokedex
- percentage_male: The percentage of the species that are male. Blank if the Pokemon is genderless.
- type1: The Primary Type of the Pokemon
- type2: The Secondary Type of the Pokemon
- height_m: Height of the Pokemon in metres
- weight_kg: The Weight of the Pokemon in kilograms
- capture_rate: Capture Rate of the Pokemon
- base_egg_steps: The number of steps required to hatch an egg of the Pokemon
- abilities: A list of abilities that the Pokemon is capable of having
- experience_growth: The Experience Growth of the Pokemon
- base_happiness: Base Happiness of the Pokemon
- against_?: Eighteen features that denote the amount of damage taken against an attack of a particular type including: bug, dark, dragon, electric, fairy, fight, fire, flying, ghost, grass, ground, ice, normal, poison, psychic, rock, steel, water.
- hp: The Base HP of the Pokemon
- attack: The Base Attack of the Pokemon
- defense: The Base Defense of the Pokemon
- sp_attack: The Base Special Attack of the Pokemon
- sp_defense: The Base Special Defense of the Pokemon
- speed: The Base Speed of the Pokemon
- generation: The numbered generation which the Pokemon was first introduced
- is_legendary: Denotes if the Pokemon is legendary.

## Section 3: Research Questions and Usage Scenarios

> The purpose of this section is to get you to think in more detail about how your target audience will use the app you're designing and to account for these detailed needs in the proposal. For this it can be helpful to create a brief persona description of a member in your intended target audience. Then, think about what they might want to do with your app and write small user story. User stories are typically written in a narrative style and include:
>
> - The specific context/background of the user
> - The overall goal of the user
> - Tasks needed to reach that goal
> - A hypothetical walkthrough of how the user would accomplish those tasks with your app
> - The outcome/action that the user would take based on the information they find in the app

John loved Pokémon as a child in the 90’s, but after growing up he’s forgotten about most of the Pokémon he once had and hasn’t kept track of the new Pokémon that have been added in more recent generations. He wants an easy, accessible method to explore the stats of different Pokémon, and see any changes that exist across different generations.

Once John visits our Pokémon dashboard he’ll see………………………………………………

Based on his time spent exploring different Pokémon in our app, John has a clearer understanding of various Pokémon stats such as height, weight, attack, defense, abilities, and more. Armed with this new knowledge, he feels confident in continuing to build his Pokémon team and battle others. He’s also excited to put this new knowledge to practice and see how his Pokémon perform.

## Section 4: App Sketch & Brief Description

![](../img/sketch.png)

The Pokémon Dashboard, provides an interactive interface for analyzing and comparing various attributes of a Pokémon with other Pokémons. It features a search bar for locating specific Pokémon, for example “Charmander”, and displays detailed information of that Pokémon. Users can filter data by generation, types (first and second) from a multi-select option. There are also range inputs to filter Pokémon by their HP, Attack, Defense, Sp. Attack, Sp. Defense, and Speed. The interface also includes a "Gotta catch em all" button which is a button to update the plots on the right side. The dashboard includes a heatmap showing the effectiveness of different types against others. There is also a section that shows scatter plots, with a drop down for different comparisons like Attack vs Speed and it is gonna show where your chosen Pokémon is. Additionally, it offers a bar chart that compares between the top 7 Pokémon based on average stats. The last one is a box plot that compares the stats by their types such as Grass, Fire, Water, and more depending on the type chosen. You can also brush on some points in the chart and tooltips are going to show up.
