# The recipe for a successful movie
### Abstract
The goal of this project is to explore the factors that contribute to a film's success. First, we will argue what success really means in the context of the film industry, considering multiple dimensions such as the box office revenue, the critical acclaim, and the ROI. We will then examine a range of factors that may influence these success metrics, including genres, casts' composition, production companies and country of origin. We aim to go beyond simple correlation and, whenever possible, establish causal relationships between these factors and movie success. This approach will help us identify elements that truly impact a film’s performance rather than coincidental associations. Additionally, we will examine how the relationship between these factors and film success has evolved over time. For instance, we will analyse the emergence and popularity of new genres, the expansion of certain international movie markets, and the prevalence of particular themes.
<br><br>

### Research questions
**Main research question:** What factors contribute to the success of a movie?

**Sub-questions:**
- How do we measure success? Is box-office the only metric? Are different metrics correlated?
- How the cast impact the success of a movie? Does the age the actors and directors impact the success of a movie? Does the gender of the cast and directors influence a movie's success? Is the diversity of a cast impactful?
- Does the genre of a movie impact its performance? Is the most successful genre always the same? Or does it change over time?
- Are there countries that produce more successful movies? Does it matter if we normalise over the number of films produced by each nation? How did this change over time?
- How much does the movie budget impact its overall performance? How important is the production company?
<br><br>

### Additional datasets
We incorporated data from three additional sources

#### 1. The Movie Database (TMDB)
- **Description:** Provides movie metadata, including revenue, budget, genres and additional attributes.
- **Source:** Downloaded from [Kaggle](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies).
- **Size:** Approximately 1.07 million entries, manageable within memory.

#### 2. Internet Movie Database (IMDB)
- **Description:** Offers comprehensive film attributes such as ratings, number of ratings, genres. In addition, it provides detailed information about the cast, including actor names, roles, and the order of importance within the film.
- **Source:** Obtained from [IMDB Non-Commercial Datasets](https://developer.imdb.com/non-commercial-datasets/).
- **Size:** The entire dataset is too large to fit into memory. To handle the dataset, we have loaded each part individually and filtered out all the non-movie entries before continuing processing the data. This process ensured that we could work agily with the dataset. The code utilized is contained in the notebook `src/scripts/imbd_dataset_filtering.ipynb`.

#### 3. Wikidata
- **Description:** We wrote a script that utilizes the [Wikidata Query Service](https://query.wikidata.org/) to automatically retrieve extensive information about movies, casts, and related people. The code utilized is contained in the notebook `src/scripts/scrape_wikidata.ipynb`.
- **Integration:** This dataset enhances our analysis with additional movies' and people's metadata and identifier mappings.

#### Combining the datasets
We have already combined these datasets into a unified dataset. The complete integration code is available in the `src/scripts` folder of the repository.
<br><br>

### Methods
**Statistical Tests**: We will use a variety of statistical tests to assess whether different groups exhibit significantly distinct properties. This includes independence tests, Z-tests for comparing group averages, and ANOVA for comparing means across multiple groups. These tests will help determine if certain film characteristics are associated with higher success metrics.

**Regression Analysis**: Both linear and logistic regression will be applied for predictive modelling and interpretation. Linear regression will help assess the relationship between quantitative variables (e.g., budget, ratings, revenue, ROI), while logistic regression will be applied for binary outcomes (e.g., the rating being above a threshold).

**Data Visualization**: We will interpret plots and try to extrapolate trends, variability, and potential outliers. We will pay particular attention to error bars and uncertainty in the data.

**Causal analysis**: Whenever investigating causality between variables, we will compute the propensity scores and use them to control for confounding factors.
<br><br>

### Timeline and organisation within the team

We expect to have about four weeks to complete the project after submitting the second homework and before the 20th December. Our work plan is as follows:

**Weeks 0 - 0.5**: In the first half week, we will focus on defining the key variables that potentially influence the success of a movie. This initial phase will involve a collaborative effort to identify and select the most impactful factors, ensuring a clear direction for the subsequent analysis.

**Weeks 0.5 - 2.5**: Over two weeks, we will conduct an in-depth analysis of these variables. To maximize efficiency, we will divide the work among team members, allowing each person to concentrate on specific aspects of the analysis. During this period, our aim is to establish strong correlations, and whenever possible, demonstrate causality using theoretical arguments and statistical methods. Despite dividing the tasks, we still plan to meet at least three times during this period to share progress, discuss findings, and ensure alignment across the team.

**Weeks 2.5 - 4**: In the final week and a half, we will consolidate our findings, create the results notebook, and write a compelling data story. This phase will involve combining the analyses, refining the visualizations, and preparing a clear, coherent narrative of our discoveries.
