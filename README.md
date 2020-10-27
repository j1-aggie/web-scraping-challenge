# Web Scraping Homework - Mission to Mars




## Power Lifting Visualization Dashboard
* [Background](#background)
* [Scraping the Web](#Scraping)
* [Visualization Dashboard Website](#MongoDB and Falsk Application)
* [Requirements](#requirements)

## <a name="background"></a>Background

In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.    

## <a name="Scraping"></a>Scraping

For the files created to perform the web scraping for the images and urls, you can go [here](https://github.com/j1-aggie/web-scraping-challenge), which will take you to the github repository for the project.  Inside the repo you will find all the visuals and working files associated with this project. The scraping process was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Request/Splinter.  The Jupyter Notebook is titled "mission_to_mars.ipynb" and was used to complete all the scraping and analysis tasks.  Below is the outline of the scraping process. 
* Nasa Mars News
    *  A. Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest news title and paragraph text.  Assigned 
           text to variables that could be referenced later. 
    *  B. Scraped the [JPL NASA GOV](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) using splinter to navigate the site and  
           find the image url for the current Featured Mars Image and assigned the url string to my variable called [featured_image_url]                                  (https://www.jpl.nasa.gov/assets/images/logo_nasa_trio_black@2x.png).
    *  C. Scraped the Mars Fact Page [here](https://space-facts.com/mars/) and used pandas to scrape the table containing facts about the              planet including Diameter, Mass, etc. Then the data was converted to a HTML table string. 
    *  D. Scraped the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) 
           to obtain high resolution images for each of Mar's hemispheres. I then found the url for full resolution for each image.  The                image url and image were both saved to the github and were also stored in Python dictionary labeled mars_dict then appended to a            list. 

## <a name="MongoDB and Flask Application"></a>MongoDB and Flask Application

To create the visualization dashboard website, I used HTML, CSS, and Bootstrap. The data was stored in the MongoDB environment. The website is currently deployed to GitHub Pages. The website works on a variety of screen sizes, from mobile to desktop. To check out the visualization dashboard website, you can go [here](https://j1-aggie.github.io/web-scraping-challenge/).  Multiple steps were taken to create a visualization page to view the images found from scraping the web.  
  *  1. Converted my jupyter notebook to a python script titled "scrape_mars.py" with a function called "scrape". Next, I created a route 
       called "/scrape" that imports my python script and calls on my scrape function.  Information that is returned is stored in Mongo as a        Python dictionary.  Then I created a root "/" that queries my Mongo database and passes the mars data into a HTML template to display        the data.
       
  *  2. Created a template HTML file called "index.html" that takes the mars data dictionary and displays all of the data in the appropriate        HTML elements.  



## <a name="requirements"></a>Requirements for Submission

The website consists of the following:

* A [jupyter notebook] containing:
  * the code to scrape the web for urls and visuals.
  * screenshots of visuals and final applications.
* A [page]for each visualization containing:
  * A descriptive title and heading.
  * The visualization.
  * A paragraph describing the plot and its significance.
 
