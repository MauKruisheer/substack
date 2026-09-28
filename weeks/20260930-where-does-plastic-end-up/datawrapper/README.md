# Interactive versions with Datawrapper

Substack can't run code, but it **can embed Datawrapper charts and maps**: paste the Datawrapper link into your post and the chart appears, interactive on the web and in the app. In emails the chart shows as an image; clicking it opens the interactive version.

These CSVs are ready to upload at https://app.datawrapper.de (free account).

## Figure 3: world map (`fig3_pollution_by_country.csv`)

1. *New Map → Choropleth map → World*.
2. *Add your data → Import your dataset*: upload the CSV. Match the column **ISO3** to *ISO-Code*.
3. Choose the value column: **Per person (kg/yr)** for 3b, or **Plastic pollution (thousand t/yr)** for 3a.
4. *Visualize → Colors*: set the type to *steps* with custom breaks, the same as the static figures:
   * total: 10, 50, 100, 500, 1000
   * per person: 0.5, 2, 5, 10, 15
5. *Tooltips*: add Country, the value, the low–high estimate, income group and "Share open burned (%)".
6. *Publish* and paste the link in Substack.

Tip: make one map with both columns and use Datawrapper's *Dropdown / Buttons* option to switch between "total" and "per person". That turns figures 3a and 3b into one interactive map.

## Figure 4: sources by income group (`fig4_pollution_sources_by_income.csv`)

1. *New Chart → Stacked Bars*. Upload the CSV.
2. *Check & Describe*: untick the columns "kg per person per year" and "Total (Mt per year)" so they aren't plotted (keep them for tooltips or labels).
3. *Refine*: turn on *Stack percentages*; order the colours as in the static figure.
