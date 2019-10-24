var width = 960,
    height = 500;

var path2 = d3.geo.path();

var svg2 = d3.select("#canvasZ").append("svg")
.attr("width", width)
.attr("height", height);

queue()
.defer(d3.json, zs)
.await(ready);

function ready(error, us) {
  svg2.append("g")
  .attr("class", "counties")
  .selectAll("path")
  .data(topojson.feature(us, us.objects.zip_codes_for_the_usa).features)
  .enter().append("path")
  .attr("class", "zip")
  .attr("data-zip", function(d) {return d.properties.zip; })
  .attr("data-state", function(d) {return d.properties.state; })
  .attr("data-name", function(d) {return d.properties.name; })
  .attr("d", path2);
}