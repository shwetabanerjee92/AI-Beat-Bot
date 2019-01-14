d3.selectAll("text")
  .on("click", function () {
    var userSelection = d3.select(this).attr("value");
    console.log(userSelection)
  });