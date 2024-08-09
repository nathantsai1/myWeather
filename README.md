# 'the good weather App'

## description
This app(it's actually a website) gives the weather, pulling information from three APIs to:
1. take all cities with the name of inputted site(taken from a 'POST' form with a text input), taking the Longitude, Latitude, city, and state/country. the name of this API was the 'geocacher', so to speak, was the openweathermap.com, which gave out small time information for free.
2. take the weather from openweathermap, just the one day.
3. take the 5 day forecast from openweathermap, to edit and send back to the hdmi templates

## how to use
1. You do need a api_key from openweathermap, and paste that with the three todos. According to the articles on this that I read, it does take a few hours to make one, but I was able to make this immediately
2. If you are not using replit, you do need to download the contents of 'requirements.txt', and python/css/js/html extension if you do not already. I used a venv, to keep these downloads in my folder, but I believe that may not be neccessary. 
3. If this is in VScode, use flask run, and click the link under the red text. If you are in Replit, click the run button, and go the networking tab, next to the console(usually on the right tab) and click the Dev URL.
I hope you enjoy this website!

## credits
Credits are due where they are needed, so here are the sources that I used:
1. Freepik
   * Many different logos(for showing the conditions of the clouds) were used, and in order, here are their authors:
   1.  Afif Fuden for this author's scattered clouds icon
   2.  Eucalyp for this author's broken clouds icon
   3.  VectorPortal for this author's shower rain icon
   4.  Freepik for this author's rainy icon
   5.  Creative Stall Premium for this author's thunderstorm icon
   *  Dreamcreateicons for this author's snowy icon
   *  Grafixpoint for this author's misty icon
2. Openweather API
   *  As stated above, this API was used in three ways.
   1. The weather
   2. The forecast
   3. The Geocacher 
3. Wikipedia
   * I'd have to say, Wikipedia was almost THE go-to source for my understanding and knowledge of the weather symbols.
4. OpenAI
   * when I did have tedious questions, and couldn't find the answers to these problems on Stack Overflow, I turned to ChatGPT for answers.
   1. One instance I remember clearly is when I tried to use jinja for if / else, and setting properties under that. It took almost two sessions, but I finally hit a lightbulb and transferred the jinja code to python lines. 
5. Figma
   * when I had many questions on what color I should use, Figma was the place to go, for their color pallete, and similar colors that made me happy, and made the color scheme what I thought the website should look like, better and more colorful.

## conclusion
I do realize that this README was long, but I am proud of my weather project. 