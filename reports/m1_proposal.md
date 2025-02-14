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

We will be visualizing a dataset with 801 rows and 41 columns. Each of the 801 rows represents a single Pokémon, and each Pokémon has 41 variables that describe its characteristics. This comprehensive set of characteristics will make it easy for our target audience (new Pokémon player) to fully understand the Pokémon that are of interest to them. The primary attributes we will focus on visualizing for each Pokémon include:

- `name`: The English name of the Pokémon
- `type1`, `type2`: The primary and secondary type (eg. Fire, Water, Grass, etc.)
- `height_m`, `weight_kg`: The height and weight
- `against_?`: Eighteen features that denote the damage taken against an attack of a particular type
- `hp`, `attack`, `defense`, `sp_attack`, `sp_defense`, `speed`: Base stats of the Pokémon
- `generation`: The video game generation that the Pokémon was introduced
- `is_legendary`: Whether the Pokémon is legendary or not

The dataset also includes several attributes that could be of interested during our visualization, such as `percentage_male`, `capture_rate`, `base_egg_steps`, `abilities`, `experience_growth`, and `base_happiness`. More information about the dataset can be found from the [Kaggle source](https://www.kaggle.com/datasets/rounakbanik/pokemon/data).

Using this data we will also derive new variables, such as the sum of the Pokémon's base stats (`base_stat_total`) as a method of ranking Pokémon overall. It would also be useful to track which Pokémon evolve into other Pokémon (`evolves_to`, `evolves_from`), but this is a complex feature to engineer. It would be interesting to see how these new features could help new Pokémon players better understand the Pokémon.

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
