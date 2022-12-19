# Cian_Avito_project

### If you wanna run this site:

* clone this repo
* **run**

```sh
npm install
```

* **run**

```sh
npm install axios
```

* **run**

```sh
npm run dev
```

* enjoy)

## About project

[Here](https://github.com/free001style/Cian_Avito_project/tree/master/parsers) there are two parsers:
for [Cian](https://www.cian.ru/) and for [Avito](https://www.avito.ru/moskva/nedvizhimost). We parsed such cities as
Moscow, SPB and Novosibirsk. We used scrapy for parsing and ScraperAPI to bypass the lock. Files cleaner.py prettify our
json and found coordinates by address(used [mapbox.Geocoder](https://docs.mapbox.com/api/search/geocoding/)).

We used [mapbox](https://www.mapbox.com/) to show flats.

Then, we made a site with a chosen city flatmap, each flat-flag shows the most important information for customers. We
provide the site user with such options: images of the flat, description, address and closest metro station, and all
this is in a convenient pop-up window.

We went further and made a mortgage calculator, FlatMap uses information from
[Sberbank](https://domclick.ru/ipoteka?from=main2022), [Alpha bank](https://alfabank.ru/get-money/mortgage/) and [VTB bank](https://www.vtb.ru/personal/ipoteka/). The
site just asks the user to fill gaps, and in return shows all the possible variants.

We used Vue.js to create our site page. The code combines CSS, HTML and JavaScript.

As an option, you can download docker image [here](https://hub.docker.com/repository/docker/free001style/cian_project).
Also there will be link/TODO.