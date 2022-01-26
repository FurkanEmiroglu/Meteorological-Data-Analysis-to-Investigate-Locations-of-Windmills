# Meteorological data analysis to determine windmill locations

### Abstract

In civil engineering, it is very important to examine meteorological data in determining whether it is economical to build a windmill in a region.

<p align="center">
  <img src="https://media3.giphy.com/media/3MbRNvfnMyUJeKGlsw/giphy.gif" alt="animated" />
</p>

In theory: 
Considering hourly wind measurements, each successive measurement direction must be adjacent in hourly direction changes for winds to be defined as a wind group (storm).

The directions considered to meet this criterion are: main directions, intermediate directions and intermediate directions of intermediate directions.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Brosen_windrose.svg/300px-Brosen_windrose.svg.png" alt="animated" />
</p>

*In simpler terms, we cannot speak of a wind group if the direction of a wind measured at 10 o'clock is not adjacent to the direction of a wind measured at 11 o'clock.*


**For instance:**

| Measurement Day |    Hour     |  Direction  |
| -----------     | ----------- | ----------- |
| Monday          | 00.00       |     ESE     |
| Monday          | 01.00       |     SE      |
| Monday		  | 02.00 		|     SE      |
| Monday          | 03.00       |     SSE     |
| Monday          | 04.00       |      S      |
| Monday          | 05.00       |      SW     |

The first five winds can be considered as a group. But the last one isn't a member of them.

-------------------------------------------------------------------------------------------------------
**Result:** \
This script examines the 2018 data of the Kuşadası / turkey meteorological station and groups the winds that meet the above-mentioned criteria. Thanks to these groupings, we can analyze the winds as storms and obtain inferences such as hourly distributions and directional distributions and make comments on whether the region is a logical choice for investment.