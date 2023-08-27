## Original Requirements
The boss wants a Traditional Chinese web-based beer recipe application that is similar to the web version of BeerSmith. The application should have version control for recipes and be able to calculate the cost for each recipe.

## Product Goals
```python
[
    "Create a web-based beer recipe application with a Traditional Chinese interface",
    "Implement version control for recipes",
    "Develop a feature to calculate the cost for each recipe"
]
```

## User Stories
```python
[
    "As a user, I want to be able to create and save my beer recipes in a web-based application",
    "As a user, I want to be able to edit my recipes and keep track of the changes",
    "As a user, I want to be able to calculate the cost of each recipe",
    "As a user, I want to be able to navigate and use the application in Traditional Chinese",
    "As a user, I want to be able to share my recipes with others"
]
```

## Competitive Analysis
```python
[
    "BeerSmith: A comprehensive beer recipe application with a wide range of features, but lacks a Traditional Chinese interface",
    "Brewtarget: An open-source beer recipe application that supports multiple languages, but lacks version control for recipes",
    "Brewer's Friend: A web-based beer recipe application with cost calculation feature, but lacks a Traditional Chinese interface",
    "Brewtoad: A beer recipe application with a large community, but lacks version control and cost calculation features",
    "Brew Recipe Developer: An application that supports recipe version control, but lacks a Traditional Chinese interface and cost calculation feature"
]
```

## Competitive Quadrant Chart
```mermaid
quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    "BeerSmith": [0.7, 0.8]
    "Brewtarget": [0.5, 0.6]
    "Brewer's Friend": [0.6, 0.7]
    "Brewtoad": [0.4, 0.5]
    "Brew Recipe Developer": [0.3, 0.4]
    "Our Target Product": [0.6, 0.8]
```

## Requirement Analysis
The product should be a web-based application that allows users to create, save, and edit beer recipes. It should also have a feature to calculate the cost of each recipe. The application should support version control for recipes and have a Traditional Chinese interface.

## Requirement Pool
```python
[
    ("Create a web-based application with a Traditional Chinese interface", "P0"),
    ("Implement version control for recipes", "P0"),
    ("Develop a feature to calculate the cost for each recipe", "P0"),
    ("Allow users to share their recipes", "P1"),
    ("Support multiple platforms (desktop, mobile)", "P2")
]
```

## UI Design draft
The application should have a clean and intuitive interface with Traditional Chinese language support. The main page should display a list of saved recipes. Each recipe should have an 'edit' button that allows users to make changes and save different versions. There should also be a 'calculate cost' button for each recipe. The layout should be responsive to fit different screen sizes.

## Anything UNCLEAR
There are no unclear points.