Note to self -

1. Create a `.dzi` file with `vips`
```
vips dzsave in.jpg dzi\out --suffix .png --tile-size 510 --vips-progress
```
2. Create and upload this to a new GitHub repository using `git`
3. Deploy this new repository using GitHub pages and wait for it to finish (makes requests faster, though not strictly necessary)
4. Change the value of `tileSources` in `index.html` to the location of the new `.dzi` file, something like
```javascript
tileSources: "https://georgetr1.github.io/BSMapData2025/out.dzi"
```
5. Commit the changes and wait for GitHub Pages to finish the new deployment
6. Verify that the new map is working on the page
7. Either delete the old files for the old map, or in the future, delete the entire repository (in future years when it's seperate)
