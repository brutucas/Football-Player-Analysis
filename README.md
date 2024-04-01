# Football-Player-Analysis

## Introduction

This data science project is going to explore the intersection of English football - not gridiron handegg - with data. I have included a backstory to help visualise the power of data - both to unearth bargains and hidden talent, but also more crucially to democratise the world. The correct application of data can prioritise those key performane metrics, potentially rewarding those footballers who are playing well and doing good things on the pitch. *How many players have missed out on opportunities to hit the big leagues, despite having feet kissed by God, due to chance, poverty, the birthplace lottery, and other similar circumstances of 'fate'?* For whatever reason, their spark got missed, the opportunity passsed, and they ended up nowhere near their potential. For various reasons, a minority of players like Jamie Vardy and N'Golo Kante have demonstrated to the sports world that talent exists, yet is regularly missed. Data can help us see with clearer, truer vision, and this is what I have shown with this project.

The questions I asked myself in the planning stage of this project: 
*Are there young, outlier footballers, who are undervalued but performing exceptionally in their respective teams and leagues?*
*Can I identify, isolate, and visualise the data for such truly talented players with bargain transfer market values?* 
*Will I be able to walk the Way of the Snake (Python) and acquire the power of 'Painted Bear' Style (Pandas) to achieve this quest?*  

Now, one problem is that player data in any of these leagues is very probably going to be skewed towards the teams performing towards the top of the table. We want to ignore those players in the top teams, such as Bayern Munich in the Bundesliga or Real Madrid in the La Liga, as they are will not be relevant to this project. I have deliberately collated a dataset of those second divisions and lesser leagues, however, if I discover during the course of my data analysis that bargain-priced players are being crowded out, I will reassess.

If I had an enormous dataset, I would include code to specifically filter out, for example, the top 3-5 clubs, whose player data will skew the results and muddy the findings.

## Identify the key metrics

### Striker

As data-scout for Shaolin.FC, we have a weighty responsibility to find excellent players going unnoticed with low transfer market values. Our target in this data project is a centre forward. Ah, the fabled number 9 position. We need a 'tip-of-the-spear' goalscorer with boots like volcanic superglue, and an uncanny ability to strike for gaps and hit the back of the net. Think someone like Harry Kane, but roughly 10 years younger and a miniscule fraction of the price.

![image](https://github.com/brutucas/Football-Player-Analysis/assets/154451874/a7cdd34e-21aa-43a8-ad35-5e0af8d9f869) A top striker with enviable stats AND even more enviable looks. Gawjus.

How are we going to find such a player in the masses of data? I got project inspiration and practical tips from an article[^fn1] that explored football data in the Serbian top-flight league to find undervalued, young players. Unless you and I are fans of this less well-known league (or, as the author writes, have "an unhealthy obsession with the Football Manager game"), it is very unlikely that we would ever notice the talented players on those lesser teams that will not traditionally challenge for a title.

So, the answer is data. This tool is reliable to identify players, who may fit the desired player profiles for Shaolin FC, from leagues not just in Serbia but around the world.[^fn2] Drawing inspiration from Scott's article, I am going to initially filter my combined dataframe for the metric '% of involvement in team goals'. 

This is a very clever metric. It does not only assess the goals scored, but also assists, which ensures that we have a complete overview of strong, attacking players. Different players have different assets and a superb playmaker can contribute enormously to his team's success without often finishing the job himself. This is obvious upon reflection, but I am learning that the potential of raw data can often lie in the choice of metric, which might (as in this case) require testing out different combinations.

My dataframe already contains the combined metric. I will complete a manual test to make sure that the data has been inputted correctly and use my burgeoning dataframe superpowers to flag any discrepancies. Once I have completed an initial analysis of involvement in team goals (for the moment, only looking at past performance of goals and assists), I will compare the results to the *expected* goals and assists to identify any overperforming players, who are not immediately visible.

This will require a filtered dataframe:
1. Remove defenders and goalkeepers and any other outfield players who have not been on the field in at least 50% of matches.
2. Only include renamed columns that are relevant to this search.[^fn3]

How do I calculate the player involvement in team goals? Firstly, I want to have the results from the data, which I will visualise in a bar chart to identify good candidates, then measure against the total goals for the player's team. The results of this calculation - '% of involvement in team goals' - will also be visualised in a bar chart. 

I will also be interested in finding out if the same players are featuring in results from '% of involvement in team expected goals'. If so, I will probably have found good candidates for deeper individual analysis.

Outliers should not be ignored. For instance, a player who has not played as many minutes, but made a disproportionate contribution to his team's success. To that end, I will create a few scatter plots with a few of the metrics to see if the data contains any surprises. 

Now is selection time! I will choose the 3-5 players that look most interesting and promising.

At this point, I will filter information from the original combined dataframe to include all of the metrics for these specific players. This will require drawing more specific, individualised data from FBref.com, such as passing, pass types, posession, and miscellaneous stats - none of which are included in the standard stats. This extra data will be cleaned and (eventually) visualised with radar charts to better understand the personal profiles of each of the 3-5 selected players. 

### Post-Project Reflections

This is an important section. I have learned an enormous amount through this project. "I'm not the data scientist I once was." Generally, I could recreate my project findings in a fraction of the time, and I found myself typing plenty of more basic code instinctively and from memory. It goes without saying, but these were BIG moments for me.

**Important Insight #1**
One of the first comments I made to my tutor was "Getting good data is super important and also super rare!" He laughed and nodded. This is obvious to anyone who hs been working for any time in he industry, but I was stunned at the widespread availability of junk and the difficulty of acquiring plentiful AND meaningful data. I need quality and quantity. No wonder Google, Fscebook, et al are selling services and products for free - the data they acquire from us is valuable. 

**Important Insight #2**
When confronted by a paywall, always check to see if there are any backdoors on the website that give access to the information (without webscraping and data piracy). This was the case on FBref.com, from which I sourced all of the player data from the various football leagues. I returned to the website a week or two after compiling the data and combining into a single dataframe, and initially struggled to find it again. I thought a paywall had been slammed down - "Was it something I said?" - and indeed, a paid subscription exists. But thankfully, no! The website was cunningly hidden elsewhere on the website - definitely a source of relief to find the data still available when I needed to check the acronyms in the column names.

**Important Insight #3**
*How do I connect my dataframe to the information source as it is refreshed with updated player data every weekend?* This was a question that cropped up a few weeks into the project, and eventually led to the hyper-focused creation (all in an eventually successful effort to get rid of the brainworm that would not let me rest) of a much larger initial footballer dataframe with data from 30+ leagues and included tier groupings to account for league difficulty. This involved delving deeper into the world of data, and setting sail to begin my illustrious (and hopefully one day infamous) career as a lawful, web-scraping 'data privateer'. God, Save the King.

**Important Insight #4**
Part of the final reflections in this project necessarily involve plenty of realising that I didn't choose the quickest or most efficient ways at the start. For example, when setting out to find a fearsome Number 9 striker for the up-and-coming Shaolin.FC, I should not only have thought about a player like Harry Kane, but actively identified and compared his stats and visualised performance profile (now that I can build radar charts). This would have helped me isolate and measure those specific metrics from the very beginning - an exciting prospect when combined with the aforementioned massive dataframe!

**Important Insight #5**
I think I was definitely overwhelmed (and at more than a few points repeatedly skullpunched) by the sheer quantity of performance metrics for footballers. Following on from the realisation that I should have created a clearer 'model striker' profile to aim towards, I also realised that I was wrong to ignore the 'Expected ___' metrics, as 1) I was overwhelmed by less-relevant metrics, and 2) did not fully understand its value. In future sports data projects, I need to take a little more time to understand the performance metrics, then filter them more wisely. 

#### Footnotes:
[^fn1]: This extremely informative article can be found on the [Total Football Analysis](https://totalfootballanalysis.com/data-analysis/data-analysis-finding-undervalued-young-players-in-the-serbian-top-flight) website, written by Lee Scott, who (as of February 2024) works as a player scout at Southampton FC. 
[^fn2]: I am late to the football data party, and nothing presented in this project is brand-spanking new or particularly groundbreaking, but I am now a data nerd (albeit uncertified). During the project, I have daydreamed more than a few times about an enormous, world-spanning dataframe with all of the datapoints available for any player and any team anywhere in the world.. *sigh* There are datasets available on websites behind steep paywalls, which will undoubtedly be used by top scouts. The broader trend in football seems to be moving away from the mere existence and vanilla usage of data, and towards the question of *how*. Which metrics should we generate and measure when everyone has access to the same data? 
[^fn3]: The columns are likely to be (in no particular order) 'goals per 90 minutes', 'assists per 90 minutes', 'goals plus assists per 90 minutes', 'expected goals per 90 minutes', 'expected assists per 90 minutes', 'expected goals plus expected assists per 90 minutes', 'position', 'age', 'total minutes'.
