# About

A personal data exploration of data collection from [Water-indexed benefits and impacts of California almonds](https://www.sciencedirect.com/science/article/pii/S1470160X17308592) using data in the ["Supplemental Information"](https://ars.els-cdn.com/content/image/1-s2.0-S1470160X17308592-mmc1.pdf) PDF.

Read about the project [here](//keelyhill.com/2021/08/21-08-nutrition-versus-water-footprint/).

# Full Data Citation

Julian Fulton, Michael Norton, Fraser Shilling,
Water-indexed benefits and impacts of California almonds,
Ecological Indicators,
Volume 96, Part 1,
2019,
Pages 711-717,
ISSN 1470-160X,
https://doi.org/10.1016/j.ecolind.2017.12.063.
(https://www.sciencedirect.com/science/article/pii/S1470160X17308592)

# Data cleanup flow
```
extract_from_pdf
        |
   clean_table
    /        \
 merge       pivot
```

# License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
