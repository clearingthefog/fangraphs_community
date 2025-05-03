# The Launch Angle Revolution May Save Lives


<!-- Hitters today focus on hitting the ball hard, and putting it in the air. Those who succeed [become stars](https://baseballsavant.mlb.com/savant-player/kyle-schwarber-656941?stats=statcast-r-hitting-mlb). Those who fail are toiling away in the low minors attempting to reinvent themselves as knuckleballers while under league investigation for illegal gambling (at least, [some of them are](https://www.washingtonpost.com/sports/2024/06/10/david-fletcher-angels-pitcher-betting/)). Though this launch-angle revolution has hurt many pitchers' stat lines, there is one small, counter-intuitive, and yet potentially much more important reason for rejoice: a decline in comebackers. -->

It's not news to anyone that being on the receiving end of a 100 mph fastball is an unpleasant experience, but it's easy for players and fans alike forget that this little projectile is in fact [a deadly weapon](https://www.baseballprospectus.com/news/article/20914/pebble-hunting-how-beanballs-and-brawls-could-be-avoided/). While the tragic death of Ray Chapman along with decades of bruises and broken bones have spurred hitters to don an array of protective items in the box, our baseball culture does not afford pitchers the same protections. This is despite the fact that batted balls regularly exceed the speeds of the fastest fastballs, and occasionally top 120 mph, which may approach the [limits of human reaction times](https://projects.seattletimes.com/2017/mariners-preview/science/) at that distance. Further, while hitters are selected for their [superhuman eyesight and reaction](https://pubmed.ncbi.nlm.nih.gov/9037989/), pitchers generally are not so endowed. The issue may be further exacerbated by ever-rising exit velocities brought on by the launch angle revolution and modern hitting analytics: 

![hard hit rates](https://raw.githubusercontent.com/clearingthefog/fangraphs_community/refs/heads/main/comebackers/figs/hard_hit_rates.jpg)

That's a concerning chart. In particular, notice the difference in scales across the panels; while the frequency of 90+ mph batted balls has increased by 8.7% in this span, 110+ mph balls occur a full 41% more often now than they did in 2015! Let's find out if this trend is putting our already-fragile pitchers at even more risk.


### Counting Black Swans
The study of comebacker injuries is greatly complicated by the miniscule sample size of such events. Although [Sports Info Solutions tracks pitcher comebacker events](https://www.sportsinfosolutions.com/2023/05/18/stat-of-the-week-pitcher-injuries-on-comebackers-on-the-rise/), only around 10 per year result in even a trainer's visit to the mound. Impacts to the head even rarer but most concerning, where a few inches can make the difference between Bobby Miller, [relatively unphased](https://www.mlb.com/news/dodgers-bobby-miller-talks-line-drive-head-injury) after a glancing 105 mph blow to forehead, and Brandon McCarthy, who [barely survived](https://www.espn.com/mlb/story/_/id/8350276/brandon-mccarthy-oakland-athletics-life-threatening-situation) a line drive to the temple in 2012.

I tackled this problem instead by looking at the much larger sample of batted balls which had the _potential_ to seriously impact a pitcher. If the rate of these "dangerous" batted balls has changed, we can assume the risk of actual injuries has changed by a proportional amount, even if our observations of actual injuries are too small to analyze. First we need a definition of "dangerous" batted balls: It's not perfect, but I settled on all line-drives which pass within three feet of the average pitcher's chest at follow-through. Since actually measuring the location of the pitcher's chest is likely impossible with publicly available data, I opted to approximate the average pitcher's follow-through as the point 55.5 feet from home plate and 4.4 feet above the ground. The former is roughly an average stride length away from the pitcher's rubber, while I estimated latter by pretending to throw a few pitches in my living room, measuring the position of my chest as a fraction of my standing height, and applying that to major league pitchers' average height (plus 5 inches for the height of the mound at that point). The three foot buffer is to account for pitchers who veer away from this point after release, such as Andrés Muñoz:

![munoz followthrough](https://raw.githubusercontent.com/clearingthefog/fangraphs_community/refs/heads/main/comebackers/figs/munoz_followthrough.png)

That's not exactly the athletic fielding position I would choose to put myself in if I had to a dodge line drives off the bat of Aaron Judge, but that's the price you pay for being able to paint 101 mph on the black.

With a bit of basic trigonometry, we can cross reference this definition with the launch angle, spray angle, and exit velocity of every batted ball in the Statcast era to determine which were potentially dangerous. The plot below shows--from the batter's perspective--the most recent 50,000 batted balls in MLB, with 95+ mph exit velocities colored blue, and 95+ mph "dangerous comebackers" colored red.

![dangerous batted balls](https://raw.githubusercontent.com/clearingthefog/fangraphs_community/refs/heads/main/comebackers/figs/batters_perspective_dangerous_balls.jpg)

The danger zone is a small but not insignificant portion of the batter's field of view, and receives a fair share of hard hit balls. The sweet spot is roughly a 5.5° launch angle to straightaway center field, which sounds about right intuitively. Let's look at a few examples to ensure our definition is working as expected:

[Video: Giancarlo Stanton, August 2nd 2018: 119.1 mph, 7° launch, -0.1° spray, 1.4 estimated feet from the average pitcher's chest](https://baseballsavant.mlb.com/sporty-videos?playId=31df2afb-0152-42a6-8d7b-fcdcb500b788)

Pretty good! A taller pitcher could have been in danger from that one.

[Video: Vlad Guerrero Jr., August 31st 2022: 118.4 mph, 4° launch, -0.9° spray, 1.8 estimated feet from the average pitcher's chest](https://baseballsavant.mlb.com/sporty-videos?playId=14b9680c-86ab-4db2-a2c5-fed729c1e2e2)

Decent. I'd eyeball the spray angle as being a little wider than statcast's estimate, but it's still close enough that it could have hit a left-handed Andrés Muñoz. The spray angles are computed from the location that the ball first hits the ground, which in some cases is different from the spray angle off the bat due to sidespin on the ball causing it to cut or tail, but the effect is usually not too strong and I don't believe Statcast gives us enough information to correct for it.


[Video: Ketel Marte, April 2nd 2025: 115.5 mph, 4° launch, -0.6° spray, 1.7 estimated feet from the average pitcher's chest](https://baseballsavant.mlb.com/sporty-videos?playId=6c5ba8d3-2966-393f-bab8-14a4ebf95be2)

That one nearly nails Carlos Rodon in the hip, but he gets just a bit of glove on it. It seems that the definition is working how we expect, now let's see what it can tell us.

### Danger Over Time

When we apply this definition to the roughly one million batted balls that have been tracked by Statcast since 2015 (ignoring 2020 as usual, though it's not out of line with the trends we identify here), we get a few thousand characterized as dangerous; the exact number depends on what exit velocity threshold is used. We'll look at 90+ and 95+ mph today, since for higher thresholds the samples become too small (we're already slicing the data pretty finely by launch and spray angle). When we plotted over time, we find a surprising trend: the rate of dangerous comebackers has decreased by 25-30% since 2015!

![dangerous batted balls per 1000 pitches](https://raw.githubusercontent.com/clearingthefog/fangraphs_community/refs/heads/main/comebackers/figs/dangerous_bb_per_pitch.jpg)

This trend has fairly strong statistical significance (p=0.03 and 0.08 respectively) and a similar pattern for both exit velocity thresholds: a large decrease in 2015-2017, and a more mixed signal since then. If the rate of dangerous comebackers was determined mostly by the rate of hard-hit balls, we'd expect it to look more like the first figure in this piece, with a fairly consistent positive trend across time. Instead, we're seeing both a different direction and shape.

Since this trend doesn't seem to be explained by exit velocity alone, let's look at our other two parameters, launch and spray angle. Here are the average launch and spray angles for all hard hit balls (not just dangerous comebackers), with spray angle normalized for batter handedness so that pulled balls are indicated by positive spray angles:

![launch and spray angle trends](https://raw.githubusercontent.com/clearingthefog/fangraphs_community/refs/heads/main/comebackers/figs/launch_and_spray.jpg)

Recall that the "danger zone" was centered on a launch of 5.5° and spray of 0°. This data shows that hard-hit balls, by any exit velocity definition, are on average being hit increasingly far from this danger zone both horizontally and vertically (all trends statistically significant with p<0.03). The largest change in launch angles occurred primarily during the 2015-2017 heyday of the so-called launch angle revolution, which explains the substantial decline in comebacker risk we found during that period, while the increasing pull tendency over time shows a slower yet steadier increase. 

Also notice from the spray angle chart that as exit velocity increases, so does the pull angle. As Davy Andrews [recently wrote](https://blogs.fangraphs.com/maybe-the-launch-angle-revolution-wasnt-really-about-launch-angle/), pulling, launching, and hitting the ball are not independent phenomena, but are in fact deeply intertwined. As bat tracking technology now confirms, meeting the ball out in front (and therefore pulling it) allows for a faster bat speed at the point of contact, and thus higher exit velocity. It also means meeting the ball further along the swing's trajectory, which results in a slightly vertical plane of attack and thus higher launch angles. These interrelated dynamics are visible in the swings of today's top hitters:

[Video: Shohei Ohtani's swing trajectory](https://streamable.com/m/analyzing-shohei-ohtani-s-home-run-through-bat-tracking-x7897)

Yet as this data shows, an unintended side effect of this tendency is that it may also help shield pitchers from the most exceptionally dangerous comebackers; the harder a ball is hit, the more likely it is to be pulled and launched away from the vulnerable pitcher. With this context, giving up a couple extra cheap homers down the line to Isaac Paredes seems like a small price for pitchers to pay. 

<!-- Lastly, one missing piece of this analysis is a deeper understanding of the relationship between comebacker velocity and risk. At the low end, a 50 mph comebacker is about as dangerous as a 60 mph comebacker (not at all). At the high end however, I suspect risk increases exponentially, though to what degree I'm not sure. Is is 10% harder to avoid a 120 mph than 100 mph? Twice as hard? Ten times? Any of those could sound plausible to me. -->



### The Shape of Comebackers to Come

While the data paints a positive picture of the trend in comebacker risk, the issue is by no means alleviated. Regardless of how rare it might be, it will only take one deadly line drive to prompt a day of reckoning in the sport. Sadly, this reactive approach to safety is standard operating procedure for baseball; it was only well after Ray Chapman's death that batting helmets were mandated, and it similarly took the 2007 death of minor league first base coach Mike Coolbaugh for MLB to require helmets for base coaches as well. 

While a few pitchers have [used protective hats](https://www.nytimes.com/2014/07/23/sports/baseball/alex-torres-is-alone-in-mlb-wearing-isoblox-hat.html), their perceived uncoolness has been the primary roadblock to wider adoption. However, history provides some optimism on this front; the arc of baseball is long, but it does bend toward safety. While there was a time when catcher's gear was [considered unmanly and possibly unsporting](https://sabr.org/journal/article/the-evolution-of-catchers-equipment/), today [catchers](https://sports.yahoo.com/article/mariners-star-unveils-special-gear-013201568.html), [batters](https://www.reddit.com/r/baseball/comments/1bqxglj/bryce_harpers_shin_guard_today_is_fantastic/), and even [umpires](https://pbs.twimg.com/media/Go65YLhbIAAap7W?format=jpg&name=small) wear an array of personalized body armors which show off individual style, flair, and personality. A similar shift in perception may eventually allow pitchers at least some degree of protection on the mound. Until then, it's a morbid waiting game to see which happens first: a brave pioneer (perhaps [Kiké Hernandez](https://www.si.com/mlb/dodgers-utility-player-enrique-hernandez-wore-helmet-pitch)) makes pitcher safety cool, or a terrible injury occurs on the mound. By reducing the risk of such a tragedy until our hero arrives, it's very possible that the launch angle revolution will save a life--or even already has.



***

_The code I used to produce this piece is available on Github [here](https://github.com/clearingthefog/fangraphs_community/tree/main/comebackers). You can reach me at laughingstock91@gmail.com._