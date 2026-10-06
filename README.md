# Shop to Stove

A personal cookbook and grocery planner. Pick recipes, see one merged shopping list with no repeated ingredients, find what you can cook with what you already have, and spot recipes that would use up what you're buying.

## What it does

- **Recipes**: browse by course, filter by one or more ingredients. A basket badge flags recipes that are close to complete with what's already on your grocery list.
- **Cook with what I have**: select the ingredients you have and see every recipe ranked by how many more you'd need to buy.
- **Grocery list**: amounts are merged across recipes and converted between units, then grouped by store section. Set servings per recipe and the quantities recalculate.
- **Settings**: choose your own staples (salt, oil, and so on), which are left out of counts and can be hidden on the list.

Your plan, servings, selections and staples are saved in your browser's local storage.

## Project layout

```
index.html      built app (open this file, or serve the folder)
images/         food photos, one per recipe, named by recipe id
src/data.js     recipe data, ingredient catalog and store sections
src/shell.html  layout, styles and app logic
build.py        combines src/ into index.html
```

## Editing

1. Change recipes in `src/data.js` or the app in `src/shell.html`.
2. Rebuild:

   ```bash
   python3 build.py
   ```

3. Open `index.html`, or serve the folder locally:

   ```bash
   python3 -m http.server 8765
   ```

Each ingredient is `[item, qty, unit, line]`: `item`, `qty` and `unit` are shopping units used to merge the grocery list, and `line` is the wording shown on the recipe page.

## Content note

The recipes and photos were transcribed from a printed cookbook for personal use. Keep this repository private and don't publish the site publicly.
