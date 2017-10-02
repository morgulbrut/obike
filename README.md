# Understanding oBike and it's business case

Working with the (strangely open) oBike API

In Juli 2017, the bike rental service oBike from Singapore started in Zurich. It
lets users rent, which ever bike they feel like, simply by scanning the
QR, and frees users of the hassle of bringing bike rentals back. The service is
sensationally cheap, charging only 1.50 Swiss Francs per half an hour. The bikes
themselves are understandbly cheaply produced, including the actual technology
involved. The API e.g. showing the real time bike location is completely
openly available. The following analysis examines the data published in
oBike API ([which has since been modified by the company](https://mobile.o.bike/api/v1/bike/list?longitude=8.541654869914055&latitude=47.37490008461292)).

The [piece appeared in the "Tages-Anzeiger"](https://www.tagesanzeiger.ch/zuerich/stadt/obikedaten-fliessen-nach-shanghai/story/31287563) on September 2017. It showed how much the companies currently earns, how long people
spend riding the bikes around the city and where they are doing so.

These were the steps involved:

1. Pulling down a snapshot of the data every 1/2 hour
2. Analysing the files and creating a origin and destination lat/longitude
3. Sending the data to the [Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/)
4. Working with the final results from the Google Distance Matrix
