var width = 960,
height = 700;

var pathcounty = d3.geo.path()
.projection(null);

var svg = d3.select("#canvasY").append("svg")
.attr("width", width)
.attr("height", height);

d3.json(us_map_locale, function(error, us) {
if (error) return console.error(error);

<!--uncomment for states-->
<!--svg.append("path")-->
<!--.datum(topojson.feature(us, us.objects.states))-->
<!--.attr("class", "land")-->
<!--.attr("d", path);-->

<!--svg.append("path")-->
<!--.datum(topojson.mesh(us, us.objects.states, function(a, b) { return a !== b; }))-->
<!--.attr("class", "borderfoo border&#45;&#45;state")-->
<!--.attr("d", path);-->

svg.append("path")
  .datum(topojson.mesh(us))
  .attr("class", "county")
  .attr("d", pathcounty);
});
