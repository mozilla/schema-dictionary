const lunr = require("lunr");
const fs = require("fs");

const args = process.argv.slice(2);
fs.readFile(args[0], (err, data) => {
  if (err) throw err;

  const idx = lunr(function buildIndex() {
    this.field("name");
    //this.field("description");

    const metrics = JSON.parse(data);
    Object.keys(metrics).forEach((id) => {
      const metric = metrics[id];
      console.log(metric.name.split(/[\._]/));
      this.add({
        id,
        name: metric.name.split(/[\._]/).join(" "),
        //description: metric.history[0].description,
      });
    });
  });
  fs.writeFileSync(args[1], JSON.stringify(idx));
  //console.log(idx.search("serp"));
});
