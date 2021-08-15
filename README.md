
# About

A personal data exploration of data collection from [Water-indexed benefits and impacts of California almonds](https://www.sciencedirect.com/science/article/pii/S1470160X17308592) using data in the ["Supplemental Information"](https://ars.els-cdn.com/content/image/1-s2.0-S1470160X17308592-mmc1.pdf) PDF.

I liked some of the charts included in the paper, but felt like more were needed to understand the absolutes of the data, not just ranking. I was interested in the total nutritional value as the resource instead of market value.

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
