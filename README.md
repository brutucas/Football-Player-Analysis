# Football-Player-Analysis

## Introduction

This data science project is going to explore the intersection of English football - not gridiron handegg - with data. I have included a backstory to help visualise the power of data - both to unearth bargains and hidden talent, but also more crucially to democratise the world. The correct application of data can prioritise those key performane metrics, potentially rewarding those footballers who are playing well and doing good things on the pitch. 

*How many players have missed out on opportunities to hit the big leagues, despite having feet kissed by God, due to chance, poverty, the birthplace lottery, and other similar circumstances of 'fate'?* For whatever reason, their spark got missed, the opportunity passsed, and they ended up nowhere near their potential. For various reasons, a minority of players like Jamie Vardy and N'Golo Kante have demonstrated to the sports world that talent exists, yet is regularly missed. Data can help us see with clearer, truer vision, and this is what I have shown with this project.

The questions I asked myself in the planning stage of this project: 
- *Are there young, outlier footballers, who are undervalued but performing exceptionally in their respective teams and leagues?*
- *Can I identify, isolate, and visualise the data for such truly talented players with bargain transfer market values?* 
- *Will I be able to walk the Way of the Snake (Python) and acquire the power of 'Painted Bear' Style (Pandas) to achieve this quest?*  

Now, one problem is that player data in any of these leagues is very probably going to be skewed towards the teams performing towards the top of the table. We want to ignore those players in the top teams, such as Bayern Munich in the Bundesliga or Real Madrid in the La Liga, as they are will not be relevant to this project. I have deliberately collated a dataset of those second divisions and lesser leagues, however, if I discover during the course of my data analysis that bargain-priced players are being crowded out, I will reassess.

Here are two examples of the initial league dataframes pre-concatenation:

![Initial 2. Bundesliga Dataframe](/Resources/Project%20Images/Screenshot%20Evidence/1.%20Initial%202.%20Bundesliga%20Dataframe.png)
![Initial Belgian Pro League Dataframe](/Resources/Project%20Images/Screenshot%20Evidence/2.%20Initial%20Belgian%20Pro%20League%20Dataframe.png)

## Identify the key metrics

### Striker

As data-scout for Shaolin.FC, I have a weighty responsibility to find excellent players going unnoticed with low transfer market values. Our target in this data project is a centre forward. Ah, the fabled number 9 position. We need a 'tip-of-the-spear' goalscorer with boots like volcanic superglue, and an uncanny ability to strike for gaps and hit the back of the net. Think someone like Harry Kane, but roughly 10 years younger and a miniscule fraction of the price.

![image](https://github.com/brutucas/Football-Player-Analysis/assets/154451874/a7cdd34e-21aa-43a8-ad35-5e0af8d9f869) 
*WOW! A top striker with enviable stats AND even more enviable looks. Gawjus.*

How are we going to find such a player in the masses of data? I got project inspiration and practical tips from an article[^fn1] that explored football data in the Serbian top-flight league to find undervalued, young players. Unless you and I are fans of this less well-known league (or, as the author writes, have "an unhealthy obsession with the Football Manager game"), it is very unlikely that we would ever notice the talented players on those lesser teams that will not traditionally challenge for a title.

So, the answer is data. This tool is reliable to identify players, who may fit the desired player profiles for Shaolin FC, from leagues not just in Serbia but around the world.[^fn2] Drawing inspiration from Scott's article, I am going to initially filter my combined dataframe for the metric '% of involvement in team goals'. 

This is a very clever metric. It does not only assess the goals scored, but also assists, which ensures that we have a complete overview of strong, attacking players. Different players have different assets and a superb playmaker can contribute enormously to his team's success without often finishing the job himself. This is obvious upon reflection, but I am learning that the potential of raw data can often lie in the choice of metric, which might (as in this case) require testing out different combinations.

This will require a filtered dataframe:
1. Identify and combine duplicate rows for players that have transferred clubs mid-season.
2. Only include renamed columns that are relevant to this search.[^fn3]

These images show the dataframe results for duplicate players and the result of combining their data into single rows.

![Identify Duplicate Players](/Resources/Project%20Images/Screenshot%20Evidence/Identify%20Duplicate%20Players.png)
![Joining Rows for Duplicate](/Resources/Project%20Images/Screenshot%20Evidence/Joining%20Rows%20for%20Duplicate.png)

Here are the final dataframes with 3000+ players ready for further filtering and analysis.

![Filtered Players Dataframe](/Resources/Project%20Images/Screenshot%20Evidence/4.%20Filtered%20Players%20Dataframe.png)
![Combined Players Dataframe](/Resources/Project%20Images/Screenshot%20Evidence/3.%20Combined%20Players%20Dataframe.png)

At this point, I am only interested in attacking players and those footballers who have been on the field in at least 50% of matches (rough calculation at this point in the season was ~13 games). Upon creating these subset dataframes, I also filtered for age to remove any strikers older than 23.

![Attacking Players Dataframe](/Resources/Project%20Images/Screenshot%20Evidence/Attacking%20Players%20Dataframe.png)
![Creating U23 Attacking Player Dataframe](/Resources/Project%20Images/Screenshot%20Evidence/Creating%20U23%20Attacking%20Player%20Dataframe.png)

I ran some checks to find the top scorers (measuring both goals *and* assists). The second image shows the results with descending data - I included the Goals per 90 to ensure as much as possible that the results were reliable and consistent.

![Top 30 U23 Scorers](/Resources/Project%20Images/Screenshot%20Evidence/Top%2030%20U23%20Scorers.png)
![Top Scorers Common](/Resources/Project%20Images/Screenshot%20Evidence/Top%20Scorers%20Common.png)

I wanted to confirm the presence of particular players, who were reappearing across multiple checks, in particular if certain top U23 strikers continued to show outlier performance stats against much older and more experienced strikers. The list was small, but proved very informative, as you can see certain names repeated across both lists.

![Best U23 Strikers](/Resources/Project%20Images/Screenshot%20Evidence/Best%20U23%20Strikers.png)
![Best U23 Scorers](/Resources/Project%20Images/Screenshot%20Evidence/Best%20U23%20Scorers.png)

*How do I calculate the player involvement in team goals?* Firstly, I want to have the results from the data, which will isolate good candidates, then measure against the total goals for the player's team. 

I will use my burgeoning dataframe superpowers to flag any discrepancies. Once I have completed an initial analysis of involvement in team goals (for the moment, only looking at past performance of goals and assists), I will compare the results to the goals and assists per 90 minutes to confirm any overperforming players, who are not immediately visible.

![Total Goal Contributions for Top 30 Attacking Players](/Resources/Project%20Images/Graph%20Images/Total%20Goal%20Contributions%20for%20Top%2030%20Attacking%20Players.png)
![Top Goal Contributions per 90 for Top 30 Attacking Players](/Resources/Project%20Images/Graph%20Images/Top%20Goal%20Contributions%20per%2090%20for%20Top%2030%20Attacking%20Players.png)

Unsurprisingly, I kept returning to goal contributions (both total and per 90) as a reliable metric for striker performance. Ultimately, it did not disappoint and I can only imagine the outlier results to be discovered with a vast dataframe filtered with these specific metrics. The charts below show the same metrics for those strikers in the desired age range.

![Goals vs Minutes Played for U23 Strikers](/Resources/Project%20Images/Graph%20Images/Goals%20vs%20Minutes%20Played%20for%20U23%20Strikers.png)
![Goal Contributions vs Minutes Played for U23 Strikers](/Resources/Project%20Images/Graph%20Images/Goal%20Contributions%20vs%20Minutes%20Played%20for%20U23%20Strikers.png)

This particular dataframe check came towards the end of the project, once I had filtered and analysed the data to identify these players of interest.

![Contribution to Team Goals](/Resources/Project%20Images/Screenshot%20Evidence/%25%20Contribution%20to%20Team%20Goals%20for%20U23%20Strikers%20of%20Interest.png)

The results of this calculation - '% of involvement in team goals' - are visualised in a bar chart, which I have also included on my Streamlit website. 

![% Contribution to Team Goals for U23 Strikers of Interest](/Resources/Project%20Images/Graph%20Images/%25%20Contribution%20to%20Team%20Goals%20for%20U23%20Strikers%20of%20Interest.png)

It goes without saying, but if the same players are featuring in results from '% of involvement in team expected goals', I will probably have found good candidates for deeper individual analysis. Outliers should not be ignored. For instance, a player who has not played as many minutes, but made a disproportionate contribution to his team's success. To that end, I will create a few scatter plots with a few of the metrics to see if the data contains any surprises. 

#### Selection time! 

At this point, I filtered information from the original combined dataframe to include all of the metrics for these specific players. I also struggled to get specific information automatically from my JupyterLab setup and opted for manual copy+paste into a Google Sheets document. This enabled me to acquire more specific, individualised data from FBref.com, such as passing, pass types, posession, and miscellaneous stats - none of which are included in the standard stats. 

This extra data was cleaned and visualised (as seen below) with various graphs (and radar charts on my Streamlit website) to better understand the personal profiles of each player of interest. I will analyse the players to find those that look most interesting and promising.

Here are several charts that show the results from a variety of checks for striker-specific performance metrics:

![Shots on Target (SOT) per 90 vs Goals per SOT for U23 Strikers of Interest](/Resources/Project%20Images/Graph%20Images/Shots%20on%20Target%20(SOT)%20per%2090%20vs%20Goals%20per%20SOT%20for%20U23%20Strikers%20of%20Interest.png)
![Aerial Duels Won (%) for U23 Strikers of Interest](/Resources/Project%20Images/Graph%20Images/Aerial%20Duels%20Won%20(%25)%20for%20U23%20Strikers%20of%20Interest.png)
![Interceptions vs Loose Balls Recovered for U23 Strikers of Interest](/Resources/Project%20Images/Graph%20Images/Interceptions%20vs%20Loose%20Balls%20Recovered%20for%20U23%20Strikers%20of%20Interest.png)
![Shot-Creating Action (SCA) Live-Ball Passes vs Goal-Creating Action (GCA) Live-Ball Passes for U23 Strikers of Interest](/Resources/Project%20Images/Graph%20Images/Shot-Creating%20Action%20(SCA)%20Live-Ball%20Passes%20vs%20Goal-Creating%20Action%20(GCA)%20Live-Ball%20Passes%20for%20U23%20Strikers%20of%20Interest.png)
![Passes Successfully Received vs Live Touches for U23 Strikers of Interest](/Resources/Project%20Images/Graph%20Images/Passes%20Successfully%20Received%20vs%20Live%20Touches%20for%20U23%20Strikers%20of%20Interest.png)

### Data-Scout Recommendations
A quick web search for the market values of the most promising U23 strikers of interest completely ruled out Thiago, Kevin Denkey, and Mohamed Amoura. Furthermore, as can be seen on the Streamlit website, their league-adjusted performance metrics (being in a weaker football league) left me with numerous question marks about their higher price tags. Now, I could be completely mistaken about the co-efficient rating for the Belgian league - in my defence, I took the rating directly from UEFA. If there are any fuming Belgians reading this, please don't shoot the messenger/data scientist - go and ask them. 

With regards to the coefficient league ratings for the German and Italian second divisions, I simply subtracted 0.25 from their respective first divisions. Both the 2. Bundesliga and Serie B were consequently more than 0.10 above the Belgian Pro League. If I have completely misjudged the coefficients, then these 3 players should obviously be considered and I would need to redo my graphs with actualised data. However, the players are out of the imaginary budget of Shaolin.FC anyway - but I want to be transparent about my conclusions and subsequent player recommendations. My expectation is that both Duesseldorf and Nuernberg would give the Belgian teams a good challenge, and possibly win. 

I am very confident that the Ligue 2 coefficient rating is realistic, and as can be seen in his radar chart, the league-adjusted stats for Andreas Hountondji appear significantly weaker. Christos Tzolis (and arguably also Can Uzun) are primarily playing in midfield or wing positions, which would perhaps completely rule them out of the candidate pool. To avoid this in future, I will filter the initial dataframe for those attackers with only 'FW' in the 'Position' column. Both are also pricey and therefore perhaps an expensive risk - certainly not a good choice for Number 9.

Peque and 

### Post-Project Reflections

This is an important section. I have learned an enormous amount through this project. "I'm not the data scientist I once was." Generally, I could recreate my project findings in a fraction of the time, and I found myself typing plenty of more basic code instinctively and from memory. It goes without saying, but these were BIG moments for me.

**Important Insight #1**
One of the first comments I made to my tutor was "Getting good data is super important and also super rare!" He laughed and nodded. This is obvious to anyone who hs been working for any time in he industry, but I was stunned at the widespread availability of junk and the difficulty of acquiring plentiful AND meaningful data. I need quality and quantity. No wonder Google, Fscebook, et al are selling services and products for free - the data they acquire from us is valuable. 

**Important Insight #2**
When confronted by a paywall, always check to see if there are any backdoors on the website that give access to the information (without webscraping and data piracy). This was the case on FBref.com, from which I sourced all of the player data from the various football leagues. I returned to the website a week or two after compiling the data and combining into a single dataframe, and initially struggled to find it again. I thought a paywall had been slammed down - "Was it something I said?" - and indeed, a paid subscription exists. But thankfully, no! The website was cunningly hidden elsewhere on the website - definitely a source of relief to find the data still available when I needed to check the acronyms in the column names.

**Important Insight #3**
*How do I connect my dataframe to the information source as it is refreshed with updated player data every weekend?* This was a question that cropped up a few weeks into the project, and eventually led to the hyper-focused creation (all in an eventually successful effort to get rid of the brainworm that would not let me rest) of a much larger, URL-connected footballer dataframe with data from 30+ leagues and included tier groupings to account for league difficulty. 

involved delving deeper into the world of data, and setting sail to begin my illustrious (and hopefully one day infamous) career as a lawful, web-scraping 'data privateer'. God, Save the King. In the future, as I mention later, if I had an enormous dataset, I would include code to specifically filter out, for example, the top 3-5 clubs, whose player data will skew the results and muddy the findings.

**Important Insight #4**
Part of the final reflections in this project necessarily involve plenty of realising that I didn't choose the quickest or most efficient ways at the start. For example, when setting out to find a fearsome Number 9 striker for the up-and-coming Shaolin.FC, I should not only have thought about a player like Harry Kane, but actively identified and compared his stats and visualised performance profile (now that I can build radar charts). This would have helped me isolate and measure those specific metrics from the very beginning - an exciting prospect when combined with the aforementioned massive dataframe!

**Important Insight #5**
I think I was definitely overwhelmed (and at more than a few points repeatedly skullpunched) by the sheer quantity of performance metrics for footballers. Following on from the realisation that I should have created a clearer 'model striker' profile to aim towards, I also realised that I was wrong to ignore the 'Expected ___' metrics, as 1) I was overwhelmed by less-relevant metrics, and 2) did not fully understand its value. In future sports data projects, I need to take a little more time to understand the performance metrics, then filter them more wisely. 

#### Footnotes:
[^fn1]: This extremely informative article can be found on the [Total Football Analysis](https://totalfootballanalysis.com/data-analysis/data-analysis-finding-undervalued-young-players-in-the-serbian-top-flight) website, written by Lee Scott, who (as of February 2024) works as a player scout at Southampton FC. 
[^fn2]: I am late to the football data party, and nothing presented in this project is brand-spanking new or particularly groundbreaking, but I am now a data nerd (albeit uncertified). During the project, I have daydreamed more than a few times about an enormous, world-spanning dataframe with all of the datapoints available for any player and any team anywhere in the world.. *sigh* There are datasets available on websites behind steep paywalls, which will undoubtedly be used by top scouts. The broader trend in football seems to be moving away from the mere existence and vanilla usage of data, and towards the question of *how*. Which metrics should we generate and measure when everyone has access to the same data? 
[^fn3]: The columns are likely to be (in no particular order) 'goals per 90 minutes', 'assists per 90 minutes', 'goals plus assists per 90 minutes', 'expected goals per 90 minutes', 'expected assists per 90 minutes', 'expected goals plus expected assists per 90 minutes', 'position', 'age', 'total minutes'.
