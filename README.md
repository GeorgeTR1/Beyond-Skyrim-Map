Note to self -

1. Create a `.dzi` file with `vips`
```
vips dzsave in.jpg dzi\out --suffix .png --tile-size 510
```
2. Create and upload this to a new GitHub repository using `git`
3. Change the value of `tileSources` in `index.html` to the location of the new `.dzi` file, something like
```javascript
tileSources: "https://raw.githubusercontent.com/GeorgeTR1/BSMapData2025/refs/heads/main/out.dzi"
```
4. Commit the changes and wait for GitHub Pages to finish the new deployment
5. Verify that the new map is working on the page
6. Either delete the old files for the old map, or in the future, delete the entire repository (in future years when it's seperate)
