# Welcome to _FORDHAM_

> Fordham is a neighborhood in the Bronx. This neighborhood contains the zip-codes 10453, 10457, 10458, 10468 and 10469. Fordham is roughly bordered by East 196th Street to the north, Webster Avenue to the east,Burnside Avenue to the south, and Jerome Avenue to the west.

### Demographics 

 _**Demographics of one sample zip-code:**_

**ZCTA5 10457**

| ZCTA5 10457              |                  |          |
|--------------------------|------------------|----------|
| _Population:_              | 74,554           |          |
| _Median Age:_             | 29.8 Years       |          |
| _Racial Breakdown:_      | 1.41%            | White    |
|                          | 29.46%           | Black    |
|                          | .12%             | AIAN     |
|                          | .91%             | Asian    |
|                          | .04%             | NHPI     |
|                          | .48%             | Other    |
|                          | 1.01%            | Two+     |
|                          | 66.57%           | Hispanic |
| _Number of Housing units:_ | 25,867           |          |
|                          | 95.23%  |  (occupied)       |
|                          | 4.77%     | (vacant)          |
| _House Value:_             | $376,600         |          |
| _Housing Unit Structure:_ | Single unit      | 4.57%    |
|                          | Multi Unit       | 95.06%   |
|                          | Mobile home      | .11%     |
|                          | Boat, RV, Van    | .24%     |

### Airbnbs in Fordham: 

<iframe src="nycMap.html" width="600" height="400" frameborder="0" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


## How to judge a neighborhood?


When considering a place to book an Airbnb, it's important to consider many of the qualities that make each neighborhood a good place to live, with some exceptions. Generally, because airbnb's usually indicate a short stay in a specific neighborhood, most of the qualities which make a neighborhood desirable in the long-term can be ignored (good schools, good doctors, best for retirees). On the other hand, there's an emphasis on benefits that can be appreciated in the short-term, such as safety and accessibility to local attractions. One feature which is more complicated is the cost of living,because, while price is important, we must still consider the demand for luxury visits, which are more desirable in a short-term destination (which Airbnb specializes in) than an actual living 
situation.

_**Three most important factors:**_

1. Safety (low crime rate)
2. Transportation (accessibility to & reliability of public transportation, ease of parking)
3. Attraction/Activities (availability of local attractions and recreational activities such as
restaurants, parks, etc.)

_**How Fordham fares:**_

_Fordham → Overall Grade: **B**_

1. _Safety:_ C (Higher crime rates than the national average in most major categories,
excluding robbery.)
2. _Transportation:_ B+ (Access to public transportation is widely available.)
3. _Attractions/Activities:_ A- (Reviewers describe a wide variety of parks, restaurants,
and other local attractions to enjoy.)

## And... Some Statistics!!

> When regarding Fordham as a borough in which to rent an Airbnb, it is interesting to visualize some of its qualities.

**1. Visualizing Price Distribution**

<img src="price%20in%20fordham%20real.png">

This graph helps to visualize the values found using the describe funciton. Additionally, a box plot provides a median, which is helpful because it does not take into consideration the outliers which are included in the data, and can skew the mean. The median price per night is approximatley $60/ night, which is less than the mean of $69/night. The maximum price (not including outliers) is $125/night, while the absolute maximum is $225/night. Most values 
lean toward the lower end of the price points. 

**2. Visualizing Room Types**

<img src="room%20in%20fordham%20real.png">

We can see that there is a strong majority of Private Rooms available, followed by entire home/apartments, and finally shared rooms.

**3. Visualizing Listing Names**

<img src="names%20in%20ford%20real.png">

I hoped to explore some part of the information we were given for the names of the Airbnb listings. I noticed as I scanned the names that many of the Airbnb’s 
mentioned their location to the Metro-North. I remembered that in HC3, much of what made an Airbnb desirable was its distance from transportation, so this seemed important. I wanted to see how many names in the dataset mentioned the metro north in their listing. I used `metro.value_counts()` to create a series
which displayed how many listing contained the word “metro” and how many did not:

```
0.0 49
1.0 13
Name: name, dtype: int64
```

I found that of the 62 listings, 13 mentioned the Metro-North. 

## Correlational Reasearch

> After seeing some trends in price and room types, it is interesting to attempt to find  correlations between price and other factors. We can use scatter plots to draw these conclusions.

**- Latitude Vs. Price**

<img src="lat%20and%20line%20in%20ford%20real.png">

The trendline reveals that there is, in fact, at least a slight positive correlation between price and increasing latitude. This is surprising, because I would think that prices would increase the closer the location is to NYC. It is possible that increasing in latitude does not exactly correspond with moving farther North from the city.


### Thanks for checking out Fordham! [Click here to head back to the Bronx, and choose another neighborhood.](https://jessicalrsparacio.github.io/TheBronx/#the-breakdown)
